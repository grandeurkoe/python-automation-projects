# Python Automation Projects

These python automation projects are built in correspondence with " [100 Days of Code - The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) " course. This course was taught by London's App Brewery top instructor Angela Yang.<br/>

Each project has been built from scratch with minimal to no assistance.<br/>

### Day 048 - Cookie Clicker

This project automates the Cookie Clicker game using the selenium package.

Steps in the automation process:
1. Navigate to the [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) website.
2. Click 🍪 every few seconds (You can set this yourself).
3. Check for any ungrayed upgrades.
4. Click on the cheapest upgrade.
5. Repeat steps 2 to 4 for 5 minutes.

![Cookie Clicker](automated-cookie-clicker/automated-cookie-clicker.gif)

### Day 049 - LinkedIn Job Application

This project automates the job application process on LinkedIn using the selenium package.

Steps in the automation process:
1. Navigate to the [LinkedIn](https://in.linkedin.com/) website.
2. Sign in to LinkedIn.
3. Search for "python developer" job listings.
4. Click "Job" tab.
5. Click "Easy Apply" filter.
6. Click on job.
7. Save job.
8. Follow company.
9. Repeat steps 6 to 8 until there are no more jobs left to click on.

![LinkedIn Job Application](automated-job-application/automated-job-application.gif)

### Day 050 - Tinder Swiping Bot

This project automates the swiping process on Tinder using the selenium package.

Steps in the automation process:
1. Navigate to the [Tinder](https://tinder.com/) website.
2. Click "Log in" button.
3. Click "Log in with Facebook" button.
4. Switch to the Facebook login window.
5. Login to Facebook.
6. Switch back to the Tinder window.
7. Click "Allow" button to give location access to Tinder.
8. Click "Enable" button to enable notifications for your Tinder profile. 
9. Swipe "Nope" a 100 times.

![Tinder Swiping Bot](auto-tinder-swiping-bot/auto-tinder-swiping-bot.gif)

### Day 051 - Internet Speed Twitter Complaint Bot

This project automates the process of fetching UP/DOWN speed from the [Speed Test](https://www.speedtest.net/) website and posts a complaint tweet on [Twitter](https://twitter.com) (If the ISP fails to fulfill it's UP/DOWN speed promise.) using the selenium package.

Steps in the automation process:
1. Navigate to the [Speed Test](https://www.speedtest.net/) website.
2. Click "GO" button.
3. Get and store UP/DOWN speed.
4. Navigate to the [Twitter](https://twitter.com/i/flow/login?lang=en) website.
5. Login to Twitter.
6. If stored UP/DOWN speed from step (3) is less than promised speed, then generate a complaint tweet.
7. Click "Post" button.

![Internet Speed Twitter Complaint Bot](internet-speed-twitter-complaint-bot/internet-speed-twitter-complaint-bot.gif)
