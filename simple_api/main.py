from fastapi import FastAPI
import random 

app = FastAPI()

# we will build two simple get endpoints
# side_hustles (provides the ideas for side hustles to user)
# money quotes (returns inspirational quotes related to wealth, success and finance)

side_hustles = [
    "Freelancing - Start offering your skills online",
    "Graphic Design - Create logos, posters, and branding materials",
    "Web Development - Build websites for clients or sell templates",
    "App Development - Develop mobile apps and sell them",
    "Selling Digital Products - Sell e-books, templates, or courses",
    "Video Editing - Edit videos for YouTubers or businesses",
    "Social Media Management - Manage social accounts for brands",
    "Blogging - Write and monetize through ads & affiliate marketing",
    "Online Tutoring - Teach subjects like math, coding, or languages",
    "Dropshipping - Sell products online without handling inventory",
    "Print-on-Demand - Design T-shirts, mugs, and sell them",
    "Affiliate Marketing - Earn commissions by promoting products",
    "Amazon FBA - Buy and resell products on Amazon",
    "Flipping Items - Resell products for profit on eBay or Facebook",
    "Selling Stock Photos - Sell your photography to stock websites",
    "Custom Jewelry Making - Create and sell handmade jewelry",
    "Teaching a Language - Offer lessons online via Zoom or platforms",
    "Creating & Selling Online Courses - Sell courses on Udemy or Teachable",
    "YouTube Channel - Create videos and earn from ads and sponsorships",
    "Podcasting - Start a podcast and monetize it",
    "Voiceover Acting - Offer voiceover services for ads and videos",
    "Stock Trading - Invest and trade in stocks for profit",
    "Crypto & NFT Investing - Buy, sell, and trade crypto and NFTs",
    "Real Estate Investing - Buy properties or rent them for income",
    "Rideshare Driving - Drive for Uber or Lyft",
    "Food Delivery - Deliver food for DoorDash or Uber Eats",
    "Pet Sitting/Dog Walking - Get paid to take care of pets",
    "Babysitting - Provide childcare services for families",
    "Event Photography - Take pictures at events and sell them",
    "Home Cleaning Services - Offer cleaning services in your area",
    "Playing Video Games for Money - Stream on Twitch or compete in eSports",
    "Mystery Shopping - Get paid to review stores and restaurants",
    "Renting Out Your Car - Rent your car on Turo",
    "Airbnb Hosting - Rent out a spare room or property"
]

money_quotes = [
    "The more you learn, the more you earn. – Warren Buffett",
    "Don't work for money; make money work for you. – Robert Kiyosaki",
    "Time is more valuable than money. – Jim Rohn",
    "Wealth consists not in having great possessions, but in having few wants. – Epictetus",
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "Financial freedom is available to those who learn about it and work for it. – Robert Kiyosaki",
    "Money is a tool. Used properly it makes something beautiful; used wrong, it makes a mess! – Bradley Vinson",
    "It’s not your salary that makes you rich; it’s your spending habits. – Charles A. Jaffe",
    "The real measure of your wealth is how much you'd be worth if you lost all your money. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Never depend on a single income. Make investment to create a second source. – Warren Buffett",
    "Empty pockets never held anyone back. Only empty heads and empty hearts can do that. – Norman Vincent Peale",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano"
]

@app.get("/side_hustles")
def get_side_hustles(api_key:str):
    """Returns a random side hustle idea."""
    if api_key != "1234567890":
        return {"error":"Invalid API key"}
    return {"side_hustle":random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(api_key:str):
    """Returns a random money quote."""
    if api_key != "1234567890":
        return {"error":"Invalid API key"}
    return {"money_quote":random.choice(money_quotes)}

