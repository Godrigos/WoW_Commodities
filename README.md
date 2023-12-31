# WoW Commodities

[![PyPI - Version](https://img.shields.io/pypi/v/wow-commodities.svg)](https://pypi.org/project/wow-commodities)
![PyPI - Downloads](https://img.shields.io/pypi/dm/WoW_Commodities)

-----

**WoW Commodities** is a tool to download [World of Warcraft](https://worldofwarcraft.blizzard.com/) commodities auction data using [Blizzard API](https://develop.battle.net/documentation).

## Installation

```console
pip install WoW_Commodities
```

## Usage

**WoW Commodities** needs tree positional arguments (in that order): 
- id: a client ID from the Blizzard API.
- secret: a secret from the Blizzard API.
- path: a writable path including the filename.

Details on how to create those credentials can be found [here](https://develop.battle.net/documentation/guides/getting-started).

**WoW Commodities** may also take optional arguments defining the region of the downloaded data. The supported regions are:

- us = North America
- eu = Europe
- kr = Korea
- tw = Taiwan
- cn = China

Defaults to `us`.

And a localization paramenter for language translations. The supported localization are:
- US Region: en_US, es_MX, pt_BR
- EU Region: en_GB, es_ES, fr_FR, ru_RU, de_DE, pt_PT, it_IT
- KR Region: ko_KR
- TW Region: zh_TW.
- CN Region: zh_CN

Bear in mind that not all combinations of Regions and Localizations are valid. For more details on those combinations read [this article](https://develop.battle.net/documentation/guides/regionality-and-apis).

Defaults to `en_US`.

With optional arguments:
```console
wow-commodities -r us -l en_US id secret C:\User\username\Downloads\data.csv.xz
```

Without optional arguments:
```console
wow-commodities id secret C:\User\username\Downloads\data.csv.xz
```

Where `id` and `secret` are your ID and SECRET from Blizzard API (alphanumerical sequences), and
`username` is your computer user. You may change this path completely if you wish, just be sure the path exists and is writable.

The downloaded data will be in a [LZMA](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm) (xz extention) compressed [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file. Once this data file can get pretty big some times.

If needed you may uncompress it with [7-Zip](https://www.7-zip.org/download.html) and use the tools of preference to analyse it, but keep in mind that several tools can read it compressed (like [R](https://cran.r-project.org/)), without the need to unpack the file. Spreadsheet software might need the uncompressed file.

P.S.: Since chinese API uses a completely diferent set of links and the server seems to have access limitations, I was unable to test it. So I can't confirm if it works for the Chinese region.

## The Data

The downloaded data consists of five columns:

- ID: a numeric identification of the auction.
- Item: a numeric identification of the item.
- Quantity: the amount of an item in the auction.
- Unit Price: the value in copper per item unit (divide by 10000 to see the value in gold). The total value of the auction can be calculated multiplying this by quantity.
- Time Left: time remaing for the auction to expire. This consists of categorical values (SHORT, MEDIUM, LONG and VERY LONG).

You can use a website like [Wowhead](https://www.wowhead.com/) to discover the item id you want to focus on. This is prefered since items can have repeated names and lots of translations, but only an unique ID. e.g: in https://www.wowhead.com/item=197794/grand-banquet-of-the-kaluak, *item=197794* is the item id you want for *Grand Banquet of Kalu'ak*.

IMPORTANT:

> Auction house data updates at a set interval. The value was initially set at 1 hour; however, it might change over time without notice.

So, it's pointless to download data in intervals lower than the API updates.

## R import Example

Below an example of a R Script to import the data. Now you can have fun with it.

```R
library(readr)

item_id = 197794 # Grand Banquet of the Kalu'ak

commodities <- read_csv(
  'C:\my\path\to\data.csv.xz',
  col_types = cols_only(
    `ID` = col_character(),
    `Item` = col_factor(),
    `Quantity` = col_integer(),
    `Unit Price` = col_double(),
    `Time Left` = col_factor(
      levels = c('SHORT', 'MEDIUM', 'LONG', 'VERY_LONG'),
      ordered = T,
    ),
  )
)

commodities$`Unit Price` <- commodities$`Unit Price` / 10000 # gold
```

You can even produce pretty cool graphics with such data.

![Graphic produced using R and ggplot.](https://i.imgur.com/LKAmPvb.jpg)

## License

**Wow Commodities** is distributed under the terms of the [LGPL 3.0](https://www.gnu.org/licenses/lgpl-3.0-standalone.html) license.

This application comes with no warrant of any kind. Use at your own risk.
