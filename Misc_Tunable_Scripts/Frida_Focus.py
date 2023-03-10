import frida
import time
import adbutils

def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])

def main():
    package_name = 'com.androidcamera.ucvm'

	# Connect to device and spawn package
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
    d = adb.device()
	
    device = frida.get_usb_device(3)
    pid = device.spawn([package_name])
    device.resume(pid)

	#Without waiting Java.perform silently fails
    time.sleep(1)

    session = device.attach(pid)

    time.sleep(1)

    script = session.create_script("""
        Java.perform(function() {
        var jeb2frida_class_init = Java.use('ggn');
        var jeb2frida_method_init = jeb2frida_class_init.$init.overload('hkc','hkd','float','boolean','ojc','int');
        jeb2frida_method_init.implementation = function(hkc0, hkd0, f, z, ojc0, v) {
                send(f.toString())
                // const ggnInstance = this.$init(hkc0, hkd0, f, z, ojc0, v); 
                // Return the new instance
                // return ggnInstance;
            };
        });
    """)

    script.on('message', on_message)
    script.load()
    input('[!] Press <Enter> at any time to detach from instrumented program.\n\n')
    session.detach()

if __name__ == '__main__':
    main()
