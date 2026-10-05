import java.io.*;
import java.net.*;

public class ClientUDP {

    public static void main(String[] args) throws IOException {

        InetAddress addr = InetAddress.getLocalHost();
        System.out.println("adresse=" + addr.getHostName());

        String s = "Hello World";
        byte[] data = s.getBytes();

        DatagramPacket packet = new DatagramPacket(data, data.length, addr, 1234);
        DatagramSocket sock = new DatagramSocket();
        sock.send(packet);

        DatagramPacket recu = new DatagramPacket(new byte[1024], 1024);
        sock.receive(recu);
        String rep = new String(recu.getData(), 0, recu.getLength());
        System.out.println("reponse=" + rep);

        sock.close();
    }
}