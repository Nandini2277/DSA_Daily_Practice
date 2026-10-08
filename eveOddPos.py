class Solution:
    def totalFine(self, date, car, fine):
        #code here
        tfine = 0
        for i in range(len(car)):
            if date % 2 == 0 and car[i] % 2 != 0:
                tfine += fine[i]
            elif date % 2 != 0 and car[i] % 2 == 0:
                tfine += fine[i]
        return tfine