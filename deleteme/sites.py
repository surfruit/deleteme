SITES_DATA = {
    # Socail networks and messengers
    "GitHub": ("https://github.com/{}", "https://github.com/settings/delete"),
    "Instagram": ("https://www.instagram.com/{}/", "https://www.instagram.com/accounts/remove/request/permanent/"),
    "TikTok": ("https://www.tiktok.com/@{}", "https://www.tiktok.com/setting/delete-account"),
    "Twitter": ("https://twitter.com/{}", "https://twitter.com/settings/deactivate"),
    "Reddit": ("https://www.reddit.com/user/{}/", "https://www.reddit.com/settings/account"),
    "Pinterest": ("https://www.pinterest.com/{}/", "https://www.pinterest.com/settings/edit/"),
    "Snapchat": ("https://www.snapchat.com/add/{}", "https://accounts.snapchat.com/accounts/delete_account"),
    "Telegram": ("https://t.me/{}", "https://my.telegram.org/auth?to=deactivate"),
    "Vkontakte": ("https://vk.com/{}", "https://vk.com/settings?act=deactivate"),
    "Facebook": ("https://facebook.com/{}", "https://www.facebook.com/help/delete_account"),

    # Professional and Creative Platforms
    "LinkedIn": ("https://www.linkedin.com/in/{}", "https://www.linkedin.com/psettings/close-account"),
    "Behance": ("https://www.behance.net/{}", "https://www.behance.net/account/delete"),
    "Dribbble": ("https://dribbble.com/{}", "https://dribbble.com/account/delete"),
    "Medium": ("https://medium.com/@{}", "https://medium.com/me/settings"),
    "Fiverr": ("https://www.fiverr.com/{}", "https://www.fiverr.com/support/articles/360010328457-Closing-your-account"),
    "Upwork": ("https://www.upwork.com/freelancers/~{}", "https://support.upwork.com/hc/en-us/articles/211062048-Close-Your-Account"),
    "About.me": ("https://about.me/{}", "https://about.me/account"),
    "Kaggle": ("https://www.kaggle.com/{}", "https://www.kaggle.com/settings"),

    # Gaming Platforms
    "Steam": ("https://steamcommunity.com/id/{}", "https://help.steampowered.com/en/wizard/HelpWithAccountData"),
    "Twitch": ("https://www.twitch.tv/{}", "https://www.twitch.tv/settings/profile"),
    "Chess.com": ("https://www.chess.com/member/{}", "https://www.chess.com/settings/closure"),
    "Roblox": ("https://www.roblox.com/users/{}/profile", "https://www.roblox.com/support"),
    "GOG": ("https://www.gog.com/u/{}", "https://support.gog.com/hc/en-us/articles/212806285-How-do-I-delete-my-GOG-account-"),
    "Origin": ("https://www.origin.com/profile/{}", "https://help.ea.com/en/help/account/how-to-close-your-ea-account/"),
    "Osu!": ("https://osu.ppy.sh/users/{}", "https://osu.ppy.sh/help/wiki/Help_Centre#accounts"),

    # Music and Media
    "SoundCloud": ("https://soundcloud.com/{}", "https://soundcloud.com/settings/extra"),
    "Spotify": ("https://open.spotify.com/user/{}", "https://support.spotify.com/article/close-account/"),
    "Last.fm": ("https://www.last.fm/user/{}", "https://www.last.fm/settings/account"),
    "Flickr": ("https://www.flickr.com/people/{}", "https://www.flickr.com/help/contact"),
    "500px": ("https://500px.com/p/{}", "https://support.500px.com/hc/en-us/articles/360009511113-How-do-I-delete-my-account-"),

    # Study and Learning Platforms
    "Duolingo": ("https://www.duolingo.com/profile/{}", "https://drive-thru.duolingo.com/"),
    "Codecademy": ("https://www.codecademy.com/profiles/{}", "https://www.codecademy.com/articles/how-do-i-delete-my-account"),
    "Coursera": ("https://www.coursera.org/user/{}", "https://learner.coursera.help/hc/en-us/articles/208280046-Close-your-account"),
    "StackOverflow": ("https://stackoverflow.com/users/{}", "https://stackoverflow.com/help/delete-account"),
    "GitLab": ("https://gitlab.com/{}", "https://gitlab.com/-/profile/account"),
    "npm": ("https://www.npmjs.com/~{}", "https://docs.npmjs.com/deleting-your-user-account"),

    # Other Popular Services
    "Letterboxd": ("https://letterboxd.com/{}/", "https://letterboxd.com/settings/deactivate/"),
    "Goodreads": ("https://www.goodreads.com/user/show/{}", "https://www.goodreads.com/user/destroy"),
    "eBay": ("https://www.ebay.com/usr/{}", "https://www.ebay.com/help/account/closing-account/closing-account?id=4191"),
    "Etsy": ("https://www.etsy.com/people/{}", "https://help.etsy.com/hc/en-us/articles/115015777068-How-to-Close-Your-Etsy-Account"),
    "Patreon": ("https://www.patreon.com/{}", "https://support.patreon.com/hc/en-us/articles/360004126311-How-do-I-delete-my-account-"),
    "ProductHunt": ("https://www.producthunt.com/@{}", "https://www.producthunt.com/settings"),
    "Wix": ("https://www.wix.com/about/contact", "https://support.wix.com/en/article/closing-your-wix-account"),
    "SlideShare": ("https://www.slideshare.net/{}", "https://www.slideshare.net/settings/account"),
    "Quora": ("https://www.quora.com/profile/{}", "https://www.quora.com/settings/privacy"),
    "Ask.fm": ("https://ask.fm/{}", "https://ask.fm/settings/deactivate-account"),

    # Cybersecurity & OSINT
    "HackerOne": ("https://hackerone.com/{}", "https://hackerone.com/settings/account"),
    "Bugcrowd": ("https://bugcrowd.com/{}", "https://bugcrowd.com/settings/account"),
    "TryHackMe": ("https://tryhackme.com/p/{}", "https://tryhackme.com/settings"),
    "HackTheBox": ("https://www.hackthebox.com/home/users/profile/{}", "https://www.hackthebox.com/home/settings/profile"),
    "LeetCode": ("https://leetcode.com/{}", "https://leetcode.com/account/"),

    # Modern Dev & Deployment
    "Vercel": ("https://vercel.com/{}", "https://vercel.com/account"),
    "Netlify": ("https://app.netlify.com/teams/{}/overview", "https://app.netlify.com/user/settings"),
    "Replit": ("https://replit.com/@{}", "https://replit.com/account"),
    "CodePen": ("https://codepen.io/{}", "https://codepen.io/settings/account"),

    # Ukrainian Services
    "Work.ua": ("https://www.work.ua/resumes/{}", "https://www.work.ua/jobseeker/my/profile/"),
    "Robota.ua": ("https://robota.ua/cv/{}", "https://robota.ua/my/profile"),
    "DOU": ("https://dou.ua/users/{}/", "https://dou.ua/users/me/settings/"),
    "Djinnu": ("https://djinni.co/q/{}", "https://djinni.co/my/profile/"),

    # New Era Socials
    "Bluesky": ("https://bsky.app/profile/{}.bsky.social", "https://bsky.app/settings"),
    "Mastodon": ("https://mastodon.social/@{}", "https://mastodon.social/settings/delete"),
    "Threads": ("https://www.threads.net/@{}", "https://help.instagram.com/171556975230303"),
}

# Adding more forums and other platforms with a generic deletion link
FORUMS_AND_OTHERS = ["forum.xda-developers.com", "bitcointalk.org", "news.ycombinator.com", "dev.to", "hashnode.com", "vimeo.com", "dailymotion.com", "disqus.com", "trello.com", "slack.com", "discord.com", "okcupid.com", "tinder.com", "badoo.com", "wattpad.com", "scribd.com", "bandcamp.com", "mixcloud.com", "reverbnation.com", "itunes.apple.com", "deviantart.com", "artstation.com", "imgur.com", "giphy.com", "photobucket.com", "shutterstock.com", "vsco.co", "strava.com", "komoot.com", "alltrails.com", "fitbit.com", "myfitnesspal.com", "booking.com", "tripadvisor.com", "airbnb.com", "couchsurfing.com", "zillow.com", "realtor.com", "houzz.com", "indiegogo.com", "kickstarter.com", "change.org", "avito.ru", "olx.ua", "prom.ua", "rozetka.com.ua"]

for site in FORUMS_AND_OTHERS:
    SITES_DATA[site] = (f"https://{site}/{{}}", f"https://google.com/search?q=how+to+delete+{site}+account")