# checkpass.py
def checkpass(input_text):
    # Add your logic here
    match input_text:
        case "texting was so hard in the olden days":
            out = "Well done you got challenge 1"
        case "1tsN0isy1nH3re":
            out = "Well done you got challenge 2"
        case "wRitEl1keaNEyGpT1aN!":
            out = "Well done you got challenge 3"
        case "80085":
            out = "Well done you got challenge 4"
        case "Qxh7+ Kf8 Qh8+ Ke7 Qe8#":
            out = "Well done you got challenge 5"
        case _:
            out = "not quite try again"
    return f"{out}"

