# checkpass.py
def checkpass(input_text):
    # Please don't look at our secret passwords, this is not an OSINT challenge
    match input_text:
        case "s0m4nyh0urs0ffun":
            out = "Well done you got challenge 1"
        case "wRitEl1keaNEyGpT1aN!":
            out = "Well done you got challenge 2"
        case "1tsN0isy1nH3re":
            out = "Well done you got challenge 3"
        case "80085":
            out = "Well done you got challenge 4"
        case "Ra1#":
            out = "Well done you got challenge 5"
        case "Ra1":
            out = "Well done you got challenge 5"
        case "texting was so hard in the olden days":
            out = "Well done you got challenge 6"
        case "1ms0n0sy":
            out = "Well done you got challenge 7"
        case "mys3cr3tAdm1r3r":
            out = "Well done you got challenge 8"
        case _:
            out = "not quite try again"
    return f"{out}"

