import segno

# qrcode = segno.make_qr('https://chat.openai.com/')
# apex = segno.make_qr('https://apex.oracle.com/pls/apex/f?p=4550:1:14040423686837:::::')
# qrcode.save("GPT.png")
# apex.save("apex.png")


# pwede nana nihao?

print("Link to QR Code Generator");

link =  input("Put your link here: ");
_qrCode = segno.make_qr(link);
_qrCode.save("QR Code.png", scale=15);

print("QR Code generated....");