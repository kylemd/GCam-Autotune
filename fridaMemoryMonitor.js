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
 
            let newoff = Libcam.begin.add(addr)                                 //Calculate new hex address for libpatcher value
            return newoff;                                                      //Return new value to routine
    },

    size() {
            return gclib.size                                                   //Return gcam lib size
    },

    ramToOffset(addr) {
        let oldoff = addr.sub(Libcam.begin).toString(16);
        return oldoff;                                                          //Return libpatcher address
}

};

const addarr = {

    rtnAddresses: function(libarg) {
        var libvalues = [];                                                     // Define empty array for pointers

        for (let i = 0; i < libarg.length; i++) {

            let addr = Libcam.offset(Number('0x' + libarg[i].address));         // Convert stored offset to match current memory address
            let bytes = Number(libarg[i].length_in_lib);

            var rng =   {                                                       // Instantiate object with base and size
                            base: addr,
                            size: bytes
                        }

            libvalues.push(rng);
            // console.log(libarg[i].address.toString(16), addr.toString(16), Libcam.ramToOffset(addr).toString(16))

        }

        return libvalues;
    },

};

const Armceptor = {

	monitormem: function(libvalues) {
		var mem = MemoryAccessMonitor.enable(
            libvalues,                                                                                      // Array of objects we made earlier
            {
                onAccess: function(details) {
                    console.log(
                        Libcam.ramToOffset(libvalues[details.rangeIndex].base).toString(16) +               // Address doesn't seem to work, so we use index to work back to libpatcher address
                        " " + details.operation + 
                        " " + details.pagesCompleted + 
                        "/" + details.pagesTotal    
                    )                                                                               
                }
            }
        );
    },
};

function memoryMonitor(liblist) {

    Libcam.init();                                                          // Get current memory offset of libgcastartup.so
    const libarg = JSON.parse(liblist);                                     // Parse API dictionary. JS array of objects.
    
    const libvalues = addarr.rtnAddresses(libarg);                          // Send the dictionary off to extract what we need

    Armceptor.monitormem(libvalues)                                         // Call memory monitor with array of objects

} 


rpc.exports = {
    monitorlibmemory: memoryMonitor
  // the name of the export (callsecretfunction) cannot have either uppercase letter nor underscores.
};