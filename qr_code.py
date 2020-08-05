import pyqrcode
import argparse
import sys



def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=str, help="name", default='qrcode')
    parser.add_argument("-c", type=str, help="content to encode", default='')
    parser.add_argument("-s", type=int, help="scale", default=6)
    parser.add_argument("-e", type=str, help="error correction choices(L, M, Q, H)", default='H')
    parser.add_argument("-v", type=int, help="version capacity 1 smallest 40 largest", default=None)
    parser.add_argument("-m", type=str, help="mode", default=None)

    """When creating a QR code only the content to be encoded is required,
       all the other properties of the code will be guessed based on the
       contents given. This function will return a :class:`QRCode` object.

       Unless you are familiar with QR code's inner workings
       it is recommended that you just specify the *content* and nothing else.
       However, there are cases where you may want to specify the various
       properties of the created code manually, this is what the other
       parameters do. Below, you will find a lengthy explanation of what
       each parameter is for. Note, the parameter names and values are taken
       directly from the standards. You may need to familiarize yourself
       with the terminology of QR codes for the names and their values to
       make sense.

       The *error* parameter sets the error correction level of the code. There
       are four levels defined by the standard. The first is level 'L' which
       allows for 7% of the code to be corrected. Second, is level 'M' which
       allows for 15% of the code to be corrected. Next, is level 'Q' which
       is the most common choice for error correction, it allow 25% of the
       code to be corrected. Finally, there is the highest level 'H' which
       allows for 30% of the code to be corrected. There are several ways to
       specify this parameter, you can use an upper or lower case letter,
       a float corresponding to the percentage of correction, or a string
       containing the percentage. See tables.modes for all the possible
       values. By default this parameter is set to 'H' which is the highest
       possible error correction, but it has the smallest available data
       capacity.

       The *version* parameter specifies the size and data capacity of the
       code. Versions are any integer between 1 and 40. Where version 1 is
       the smallest QR code, and version 40 is the largest. If this parameter
       is left unspecified, then the contents and error correction level will
       be used to guess the smallest possible QR code version that the
       content will fit inside of. You may want to specify this parameter
       for consistency when generating several QR codes with varying amounts
       of data. That way all of the generated codes would have the same size.

       The *mode* parameter specifies how the contents will be encoded. By
       default, the best possible mode for the contents is guessed. There
       are four possible modes. First, is 'numeric' which is
       used to encode integer numbers. Next, is 'alphanumeric' which is
       used to encode some ASCII characters. This mode uses only a limited
       set of characters. Most problematic is that it can only use upper case
       English characters, consequently, the content parameter will be
       subjected to str.upper() before encoding. See tables.ascii_codes for
       a complete list of available characters. The is 'kanji' mode can be
       used for Japanese characters, but only those that can be understood
       via the shift-jis string encoding. Finally, we then have 'binary' mode
       which just encodes the bytes directly into the QR code (this encoding
       is the least efficient).

       The *encoding* parameter specifies how the content will be interpreted.
       This parameter only matters if the *content* is a string, unicode, or
       byte array type. This parameter must be a valid encoding string or None. 
       t will be passed the *content*'s encode/decode methods.
       """

    # error = 'H', version = None, mode = None, encoding = None
    args = parser.parse_args()

    if args.c != "":
        print("created qr codes")

        # Generate QR code
        qr = pyqrcode.create(content=args.c, mode=args.m, version=args.v, error=args.e)

        qr.svg(f"{args.n}.svg", scale=args.s)

        qr.png(f"{args.n}.png", scale=args.s)
    else:
        print('-c must provide string to encode')
        print('qr_code.py -c <content to encode> -n <name> -v <version> -s <scale> -e <error correction> -m <mode>')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])