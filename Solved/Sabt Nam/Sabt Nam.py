# ثبت نام
# ID : 21205
# https://quera.org/problemset/21205/
# https://b2n.ir/p71041

def check_registration_rules(**kwargs):
    h = []

    for i in kwargs:
        if i != "quera" and i != "codecup" and len(i) >= 4:
            if len(kwargs[i]) >= 6:
                if kwargs[i].isdigit() == False:
                    h.append(i)

    return h
