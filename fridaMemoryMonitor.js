/// <reference path="frida-gum.d.ts" />

const libCam = {

    init() {
 
        //Find GCam lib. Make sure you have libpatcher off!
            let lib_ram = Process.findModuleByName("libgcastartup.so");

        //Calculate lib size
            libCam.begin = lib_ram.base;
            libCam.size = lib_ram.size;
            libCam.end = libCam.begin.add(libCam.size);

    },

    offset(ram_addr) {
 
            var new_offset = libCam.begin.add(ram_addr)                                 //Calculate new hex address for libpatcher value
            return new_offset;                                                      //Return new value to routine
    },

    size() {
            return gclib.size                                                   //Return gcam lib size
    },

    ramToOffset(ram_addr) {
        var lib_offset = ram_addr.sub(libCam.begin).toString(16);
        return lib_offset;                                                          //Return libpatcher address
    }
};

function returnAddrs(api_obj) { 
    var rtn_addresses = [];                                                     // Define empty array for pointers

    for (let i = 0; i < api_obj.length; i++) {

        let addr_pointer = new NativePointer(libCam.offset('0x' + api_obj[i].address));         // Convert stored offset to match current memory address
        let addr_size = api_obj[i].length_in_lib;

        var rtn =   {                                                       // Instantiate object with base and size
                        base: addr_pointer,
                        size: addr_size
                    }

        rtn_addresses.push(rtn);

    }

    return rtn_addresses;
};

function returnNames(api_obj) {
    var rtn_names = [];                                                     // Define empty array for pointers

    for (let i = 0; i < api_obj.length; i++) {

        rtn_names.push(api_obj[i].name);

    }

    return rtn_names;
};

function monitorMem(address_obj,names_arr) {

    MemoryAccessMonitor.enable(
        address_obj,                                                                                      // Array of objects we made earlier
        {
            onAccess: function(details) {
                
                let lib_from = libCam.ramToOffset(details.from);
                let lib_index = libCam.ramToOffset(address_obj[details.rangeIndex].base).toString(16);      //Frida doesnt seem to return the correct ram address so we use by index.
                let lib_name = names_arr[details.rangeIndex];                                                //The names are in the same return order so just use array
                
                console.log(

                    lib_index + '\t\t' + details.operation + '\t\t' + lib_from + '\t\t' + details.pagesCompleted + '\t\t' + details.pagesTotal + '\t\t' + lib_name 

                );

                // let index = address_obj[details.rangeIndex].base;                                           //Attempt at resuming monitoring on hit address
                // let size = address_obj[details.rangeIndex].size;
                
                // monitorMem( { base: index, size: size } );

            }
        }
    );
};

function memoryMonitor(api_list) {

    libCam.init();                                                          // Get current memory offset of libgcastartup.so
    var api_obj = JSON.parse(api_list);                                       // Parse API dictionary. JS array of objects.
    var address_obj = returnAddrs(api_obj);                          // Parse addresses out of dict
    var names_arr = returnNames(api_obj);                           // Parse addresses and matching names from dict

    monitorMem(address_obj,names_arr);                               // Call memory monitor with address object array and name array

} 


rpc.exports = {
    monitorlibmemory: memoryMonitor
  // the name of the export (callsecretfunction) cannot have either uppercase letter nor underscores.
};