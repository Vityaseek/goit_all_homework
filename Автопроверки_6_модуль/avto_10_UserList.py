from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum([i for i in self.data])


payment = AmountPaymentList([i for i in range(10)])

print(payment)
print(payment.amount_payment())
