#get user email addess
email=input("What is your email address?: ").strip()


#slice out user name
user=email[:email.index("@"):]

#slice out domain name (+1 is added to exclude "@' from domain else it would have have start with "@")
domain=email[email.index("@")+1:]

#format message
#method1
output="Your username is {} and your domain name is {}"
message=output.format(user, domain)

#method2
output="Your username is {} and your domain name is {}".format(user, domain)

#display output message
#method1
print(message)

#method2
print(output)
