/// <reference path="frida-gum.d.ts" />

const Libcam = {

    init() {
 
        //Find GCam lib. Make sure you have libpatcher off!
            let gclib = Process.findModuleByName("libgcastartup.so");

        //Calculate lib size
            Libcam.begin = gclib.base;
            Libcam.size = gclib.size;
            Libcam.end = Libcam.begin.add(Libcam.size);

        //Echo values to console for debugging
            // console.log('Lib stats:')
            // console.log('Size (bytes):' + gclib.size);
            // console.log('Base address:' + gclib.base);
            // console.log('End address:' + Libcam.end);

    },

    offset(addr) {

        //Calculate new hex address for libpatcher value 
            let newoff = Libcam.begin.add(addr) 

        //Echo new offset for debugging
            console.log('New offset of libpatcher value is:' + newoff)

        //Return new value to routine
            return newoff;
    },

    size() {
        //Return gcam lib size
            return gclib.size
    }

};

const Armceptor = {

	writemem: function(addr,newhex) {
		Memory.patchCode(addr, 4, code => {
            const writer = new Arm64Writer(code, { pc: addr });

            writer.putInstruction(newhex); //Replace with newhex when confirmed working
            writer.flush();
        })
	},

	readmem: function(addr,size) {
        let results = hexdump(addr, {
            offset: 0,
            length: size,
            header: false,
            ansi: false
            });
        console.log(results);
    }

};

function swap32(val) {
    return ((val & 0xFF) << 24)
           | ((val & 0xFF00) << 8)
           | ((val >> 8) & 0xFF00)
           | ((val >> 24) & 0xFF);
};

const LibPatcher = {
    patch_hex(libaddr, newhex) {

        libaddr = Number('0x' + libaddr)
        newhex = swap32(Number('0x' + newhex))

        Armceptor.writemem(Libcam.offset(libaddr),newhex);
        Armceptor.readmem(Libcam.offset(libaddr),4);
    }
}



function patchlibaddrs(libaddr, newhex) {

    Libcam.init();
    LibPatcher.patch_hex(libaddr,newhex);
}

function getPhotoName() {
    Interceptor.attach(Module.findExportByName("libgcastartup.so", ".fileno"), {
        onEnter: function(args) {
          this.flag = false;
          var filename = Memory.readCString(ptr(args[0]));
          console.log('filename =', filename)
          if (filename.endsWith(".jpg")) {
            this.flag = true;
            var backtrace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join("\n\t");
            console.log("file name [ " + Memory.readCString(ptr(args[0])) + " ]\nBacktrace:" + backtrace);
          }
        },
        onLeave: function(retval) {
          if (this.flag) // passed from onEnter
            console.warn("\nretval: " + retval);
        }
      });
}

rpc.exports = {
    libpatcher: patchlibaddrs,
    getphotoname: getPhotoName
  // the name of the export (callsecretfunction) cannot have either uppercase letter nor underscores.
};