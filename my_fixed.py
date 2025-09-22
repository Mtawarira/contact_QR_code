import qrcode
import vobject

## CONSTANTS

F_NAME = "Mqhele"  # Your first name
L_NAME = "Mtawarira"  # Your last name
EMAIL = "mtawarira@gmail.com"  # Your email address
MOBILE = "+27635061881"  # Your mobile number
WEBSITE = "https://www.engsol.college"  # Your website URL
TELEPHONE = "+264816355719"  # Your telephone number
STREET_ADDRESS = "PO Box 25913, Windhoek. Windhoek"  # Your street address
SUBURB = "Windhoek North"  # Your suburb
CITY = "Windhoek"  # Your city
STATE = "Namibia"  # Your state
ZIP_CODE = "10001"  # Your zip code
FILENAME = "MyQR.png"

## Create vCard

vcard = vobject.vCard()
vcard.add("n")
vcard.n.value = vobject.vcard.Name(given=F_NAME, family=L_NAME)  # First name and last name are separated
vcard.add("fn")
vcard.fn.value = f"{F_NAME} {L_NAME}"
vcard.add("email")
vcard.email.value = EMAIL
vcard.add("tel")
vcard.tel.value = MOBILE
vcard.add("url")
vcard.url.value = WEBSITE
vcard.add("tel")  # Add telephone number
vcard.tel.type_param = "WORK"  # Set the type of telephone number
vcard.tel.value = TELEPHONE
vcard.add("adr")  # Add address
vcard.adr.value = vobject.vcard.Address(
    street=STREET_ADDRESS,
    city=CITY,
    region=STATE,
    code=ZIP_CODE,
    #country="SA"  # Change the country as needed
)

## Create QR Code image

image = qrcode.make(vcard.serialize())
image.save(FILENAME)
