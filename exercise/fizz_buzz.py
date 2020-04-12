class FizzBuzz:
    def return_fizz_buzz(self, number):
        if int(number) % 3 == 0:
            if int(number) % 5 != 0:
                output = 'fizz'
            else:
                output = 'fizz-buzz'
        else:
            if int(number) % 5 != 0:
                output = number
            else:
                output = 'buzz'
        return output


