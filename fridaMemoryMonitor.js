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

        //Return new value to routine
            return newoff;
    },

    size() {
        //Return gcam lib size
            return gclib.size
    }

};

const Armceptor = {

	monitormem: function(ramaddr, ramlength) {
		var mem = MemoryAccessMonitor.enable(
            {
                base: ramaddr,
                size: ramlength
            },
            {
                onAccess: function(details) {
                    console.log(
                        details.address + "," + details.operation + "," + details.from.sub(base_addr) + "," + pagesCompleted + "/" + pagesTotal
                    )               
                }
            }
        );
        mem.wait();
    },
};

function putRamtoArray(libaddr) {
        let i = 0;
        for (i = 0; i < libaddr.length; i++) {
            libaddr[i] = Libcam.offset(Number(libaddr[i]));
        }
}

function strToNum(hexlength) {
        let i = 0;
        for (i = 0; i < hexlength.length; i++) {
            hexlength[i] = Number(hexlength[i]);
        }
}

const memoryMon = {
    watch_hex(libaddr, hexlength) {

        let ramaddr = putRamtoArray(libaddr)
        let ramlength = strToNum(hexlength)
        Armceptor.monitormem(ramaddr,ramlength);
    }
}


function memoryMonitor(libaddr, hexlength) {

    Libcam.init();
    memoryMon.watch_hex(libaddr, hexlength);
}

rpc.exports = {
    monitorlibmemory: memoryMonitor
  // the name of the export (callsecretfunction) cannot have either uppercase letter nor underscores.
};