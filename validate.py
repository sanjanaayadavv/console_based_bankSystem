def validate_pan_card(pan_card):
    if len(pan_card) == 10 and pan_card.isalnum() and pan_card[:5].isalpha() and pan_card[5:9].isdigit() and pan_card[9].isalpha():
        return True
    else:
        return False

def validate_account_number(account_number):
    if len(account_number) == 10 and account_number.isdigit():
        return True
    else:
        return False

def validate_ifsc_code(ifsc_code):
    if len(ifsc_code) == 11 and ifsc_code[:4].isalpha() and ifsc_code[4:].isdigit():
        return True
    else:
        return False

def validate_gender(gender):
     if gender == "Male" or gender == "Female":
          return True
     else:
          return False


def validate_aadhar_card(aadhar_card):
    if len(aadhar_card) == 12 and aadhar_card.isdigit():
        return True
    else:
        return False