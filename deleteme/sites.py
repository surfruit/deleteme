SITES_DATA = {
    # Соцмережі та Месенджери
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

    # Професійні та Творчі
    "LinkedIn": ("https://www.linkedin.com/in/{}", "https://www.linkedin.com/psettings/close-account"),
    "Behance": ("https://www.behance.net/{}", "https://www.behance.net/account/delete"),
    "Dribbble": ("https://dribbble.com/{}", "https://dribbble.com/account/delete"),
    "Medium": ("https://medium.com/@{}", "https://medium.com/me/settings"),
    "Fiverr": ("https://www.fiverr.com/{}", "https://www.fiverr.com/support/articles/360010328457-Closing-your-account"),
    "Upwork": ("https://www.upwork.com/freelancers/~{}", "https://support.upwork.com/hc/en-us/articles/211062048-Close-Your-Account"),
    "About.me": ("https://about.me/{}", "https://about.me/account"),
    "Kaggle": ("https://www.kaggle.com/{}", "https://www.kaggle.com/settings"),

    # Геймінг та Стрімінг
    "Steam": ("https://steamcommunity.com/id/{}", "https://help.steampowered.com/en/wizard/HelpWithAccountData"),
    "Twitch": ("https://www.twitch.tv/{}", "https://www.twitch.tv/settings/profile"),
    "Chess.com": ("https://www.chess.com/member/{}", "https://www.chess.com/settings/closure"),
    "Roblox": ("https://www.roblox.com/users/{}/profile", "https://www.roblox.com/support"),
    "GOG": ("https://www.gog.com/u/{}", "https://support.gog.com/hc/en-us/articles/212806285-How-do-I-delete-my-GOG-account-"),
    "Origin": ("https://www.origin.com/profile/{}", "https://help.ea.com/en/help/account/how-to-close-your-ea-account/"),
    "Osu!": ("https://osu.ppy.sh/users/{}", "https://osu.ppy.sh/help/wiki/Help_Centre#accounts"),

    # Музика та Фото
    "SoundCloud": ("https://soundcloud.com/{}", "https://soundcloud.com/settings/extra"),
    "Spotify": ("https://open.spotify.com/user/{}", "https://support.spotify.com/article/close-account/"),
    "Last.fm": ("https://www.last.fm/user/{}", "https://www.last.fm/settings/account"),
    "Flickr": ("https://www.flickr.com/people/{}", "https://www.flickr.com/help/contact"),
    "500px": ("https://500px.com/p/{}", "https://support.500px.com/hc/en-us/articles/360009511113-How-do-I-delete-my-account-"),

    # Навчання та Технології
    "Duolingo": ("https://www.duolingo.com/profile/{}", "https://drive-thru.duolingo.com/"),
    "Codecademy": ("https://www.codecademy.com/profiles/{}", "https://www.codecademy.com/articles/how-do-i-delete-my-account"),
    "Coursera": ("https://www.coursera.org/user/{}", "https://learner.coursera.help/hc/en-us/articles/208280046-Close-your-account"),
    "StackOverflow": ("https://stackoverflow.com/users/{}", "https://stackoverflow.com/help/delete-account"),
    "GitLab": ("https://gitlab.com/{}", "https://gitlab.com/-/profile/account"),
    "npm": ("https://www.npmjs.com/~{}", "https://docs.npmjs.com/deleting-your-user-account"),

    # Інші популярні ресурси
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
}

# Додамо ще 50+ сайтів динамічно для масштабу
FORUMS_AND_OTHERS = ["forum.xda-developers.com", "bitcointalk.org", "news.ycombinator.com", "dev.to", "hashnode.com", "vimeo.com", "dailymotion.com", "disqus.com", "trello.com", "slack.com", "discord.com", "okcupid.com", "tinder.com", "badoo.com", "wattpad.com", "scribd.com", "bandcamp.com", "mixcloud.com", "reverbnation.com", "itunes.apple.com", "deviantart.com", "artstation.com", "imgur.com", "giphy.com", "photobucket.com", "shutterstock.com", "vsco.co", "strava.com", "komoot.com", "alltrails.com", "fitbit.com", "myfitnesspal.com", "booking.com", "tripadvisor.com", "airbnb.com", "couchsurfing.com", "zillow.com", "realtor.com", "houzz.com", "indiegogo.com", "kickstarter.com", "change.org", "avito.ru", "olx.ua", "prom.ua", "rozetka.com.ua"]

for site in FORUMS_AND_OTHERS:
    SITES_DATA[site] = (f"https://{site}/{{}}", f"https://google.com/search?q=how+to+delete+{site}+account")