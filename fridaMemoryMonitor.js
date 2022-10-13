/// <reference path="frida-gum.d.ts" />

const Libcam = {

    init() {
 
        //Find GCam lib. Make sure you have libpatcher off!
            let gclib = Process.findModuleByName("libgcastartup.so");

        //Calculate lib size
            Libcam.begin = gclib.base;
            Libcam.size = gclib.size;
            Libcam.end = Libcam.begin.add(Libcam.size);

    },

    offset(addr) {
 
            let newoff = Libcam.begin.add(addr) //Calculate new hex address for libpatcher value
            return newoff;                      //Return new value to routine
    },

    size() {
            return gclib.size                   //Return gcam lib size
    }

};

const Armceptor = {

	monitormem: function(monitorObjects) {
		var mem = MemoryAccessMonitor.enable(
            monitorObjects,
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
    watch_hex(liblist) {

        let ramaddr = putRamtoArray(liblist)
        let ramlength = strToNum(hexlength)
        Armceptor.monitormem(ramaddr,ramlength);
    }
}

function memoryMonitor(liblist) {

    Libcam.init();                                                  // Get current memory offset of libgcastartup.so
    let libarg = JSON.parse(liblist);                               // Parse API dictionary. Seems to be object of arrays...
    
    // console.log(JSON.stringify(libarg));                         // This works which means it's a JS object

    var libvalues = []

    for (let i = 0; i < libarg.length; i++) {
        console.log(JSON.stringify(libarg[i]))                      // This also works which means each lib value is a JS object
        libvalues.push(libarg["address"],libarg["length_in_lib"]);  // If that's the case then this should work
    } 

    for (let i = 0; i < libvalues.length; i++) {
        console.log(libvalues[i]);                                  // But then this doesn't work
    } 

    // const arrArr = libobject.map(x => Object.values(x));

    // console.log(arrArr.address);

    // var result = [];

    // for(var i in liblist)
    //     result.push([liblist.address[i],liblist.length_in_lib[i]]);

}

rpc.exports = {
    monitorlibmemory: memoryMonitor
  // the name of the export (callsecretfunction) cannot have either uppercase letter nor underscores.
};