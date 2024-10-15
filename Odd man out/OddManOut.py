def alone_Guest():
    testCase = int(input())

    if (1<=testCase<=50 ):
        test = {}
        for i in range(testCase):
            guestsNum = int(input())
            invitcode = list(map(int, input().split()))
            if (3<=guestsNum<=1000) and (len(invitcode) == guestsNum):
                test[i] = invitcode
            else:
                print("error, start again")
                alone_Guest() 
        for j in range(len(test)):
            unique = 0
            for number in test[j]:
                unique ^= number
            print(f"Case #{j+1}: {unique}")
        return()
    else:
        print("error, start again")
        alone_Guest()        

alone_Guest()

