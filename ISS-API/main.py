import requests
import smtplib

iss_url = "http://api.open-notify.org/iss-now.json"

my_email = "stamnoob@gmail.com"
rec_email = ["stamatios.tzanos@gmail.com", "candilupus@gmail.com", "dimtzanos@gmail.com"]
pwrd = "buwrzileuxevbowd"

def main():
    response = requests.get(url=iss_url)
    response.raise_for_status()

    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    if (16 < int(longitude) < 30) and (30 < int(latitude) < 45):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # encryption for security
            connection.login(user=my_email, password=pwrd)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=rec_email,
                msg="Subject:ISS IS OVER GREECE!\n\n Watch here: \n https://www.youtube.com/watch?v=86YLFOog4GM"
            )
    else:
        print("ISS is not over Greece...")


if __name__ == '__main__':
    main()
