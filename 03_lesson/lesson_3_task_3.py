from address import Address
from mailing import Mailing


address1 = Address("12508", "Москва", "Планетная", "4", "157")
address2 = Address("630099", "Новосибирск", "Красный проспект", "10", "686")
mailing = Mailing(address1, address2, track="ru159", cost=15000)

print(mailing.__str__())
