class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"  # !r calls the repr method of self.name

    def disconnect(self):
        self.connected = False
        print("Disconnected")


printer = Device("Printer", "USB")
print(printer)  # Device 'Printer' (USB)
printer.disconnect()  # Disconnected


class Printer(Device):  # inherits from Device
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity  # max capacity
        self.remaining_pages = capacity  # current capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"  # super prints str from device + pages remaining

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return  # exit if not connected
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)  # Printing 20 pages.
print(printer)  # Device 'Printer' (USB) (480 pages remaining)

printer.disconnect()
printer.print(30)  # Your printer is not connected.
