from scapy.all import IP, ICMP, send
import tkinter as tk
from tkinter import messagebox

def send_icmp_packet():
    target_ip = entry_ip.get()
    packet_count = entry_count.get()
    
    if not target_ip:
        messagebox.showerror("Error", "Please enter a target IP address or hostname.")
        return

    if not packet_count.isdigit() or int(packet_count) <= 0:
        messagebox.showerror("Error", "Please enter a valid number of packets.")
        return

    try:
        # Create an IP packet
        ip_packet = IP(dst=target_ip)
        
        # Create an ICMP packet
        icmp_packet = ICMP()
        
        # Combine the IP and ICMP packets
        packet = ip_packet / icmp_packet
        
        # Send the packet the specified number of times
        for _ in range(int(packet_count)):
            send(packet, verbose=False)
        
        messagebox.showinfo("Success", f"{packet_count} ICMP packet(s) sent to {target_ip}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("The Smurf 1.0 ICMP Packet Sender")

# Create and place widgets
tk.Label(root, text="Enter target IP or hostname:").pack(pady=5)
entry_ip = tk.Entry(root, width=30)
entry_ip.pack(pady=5)

tk.Label(root, text="Enter number of packets:").pack(pady=5)
entry_count = tk.Entry(root, width=10)
entry_count.pack(pady=5)

send_button = tk.Button(root, text="Send ICMP Packet", command=send_icmp_packet)
send_button.pack(pady=10)

# Run the application
root.mainloop()