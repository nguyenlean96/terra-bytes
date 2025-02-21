import os
import json
import string
from collections import defaultdict

COUNTRY_NAME = {
    '':  'Unknown',
    'AD':  'Andorra',
    'AE':  'United Arab Emirates',
    'AF':  'Afghanistan',
    'AG':  'Antigua and Barbuda',
    'AI':  'Anguilla',
    'AL':  'Albania',
    'AM':  'Armenia',
    'AO':  'Angola',
    'AQ':  'Antarctica',
    'AR':  'Argentina',
    'AS':  'American Samoa',
    'AT':  'Austria',
    'AU':  'Australia',
    'AW':  'Aruba',
    'AX':  'Åland Islands',
    'AZ':  'Azerbaijan',
    'BA':  'Bosnia and Herzegovina',
    'BB':  'Barbados',
    'BD':  'Bangladesh',
    # Page 2
    'BE':  'Belgium',
    'BF':  'Burkina Faso',
    'BG':  'Bulgaria',
    'BH':  'Bahrain',
    'BI':  'Burundi',
    'BJ':  'Benin',
    'BL':  'Saint Barthélemy',
    'BM':  'Bermuda',
    'BN':  'Brunei Darussalam',
    'BO':  'Bolivia (Plurinational State of)',
    'BQ':  'Bonaire, Sint Eustatius and Saba',
    'BR':  'Brazil',
    'BS':  'Bahamas',
    'BT':  'Bhutan',
    'BW':  'Botswana',
    'BY':  'Belarus',
    'BZ':  'Belize',
    'CA':  'Canada',
    'CC':  'Cocos (Keeling) Islands',
    'CD':  'Congo, Democratic Republic of the',
    # Page 3
    'CF':  'Central African Republic',
    'CG':  'Republic of the Congo',
    'CH':  'Switzerland',
    'CI':  'Ivory Coast',
    'CK':  'Cook Islands',
    'CL':  'Chile',
    'CM':  'Cameroon',
    'CN':  'People\'s Republic of China',
    'CO':  'Colombia',
    'CR':  'Costa Rica',
    'CU':  'Cuba',
    'CV':  'Cape Verde',
    'CW':  'Curaçao',
    'CX':  'Christmas Island',
    'CY':  'Cyprus',
    'CZ':  'Czech Republic',
    'DE':  'Germany',
    'DJ':  'Djibouti',
    'DK':  'Denmark',
    'DM':  'Dominica',
    # Page 4
    "DO":  "Dominican Republic",
    "DZ":  "Algeria",
    "EC":  "Ecuador",
    "EE":  "Estonia",
    "EG":  "Egypt",
    "EH":  "Western Sahara",
    "ER":  "Eritrea",
    "ES":  "Spain",
    "ET":  "Ethiopia",
    "FI":  "Finland",
    "FJ":  "Fiji",
    "FK":  "Falkland Islands (Malvinas)",
    "FM":  "Micronesia, Federated States of",
    "FO":  "Faroe Islands",
    "FR":  "France",
    "GA":  "Gabon",
    "GB":  "United Kingdom of Great Britain and Northern Ireland",
    "GD":  "Grenada",
    "GE":  "Georgia",
    "GF":  "French Guiana",
    # Page 5
    "GG":  "Guernsey",
    "GH":  "Ghana",
    "GI":  "Gibraltar",
    "GL":  "Greenland",
    "GM":  "Gambia",
    "GN":  "Guinea",
    "GP":  "Guadeloupe",
    "GQ":  "Equatorial Guinea",
    "GR":  "Greece",
    "GS":  "South Georgia and the South Sandwich Islands",
    "GT":  "Guatemala",
    "GU":  "Guam",
    "GW":  "Guinea-Bissau",
    "GY":  "Guyana",
    "HK":  "Hong Kong",
    "HN":  "Honduras",
    "HR":  "Croatia",
    "HT":  "Haiti",
    "HU":  "Hungary",
    "ID":  "Indonesia",
    # Page 6
    'IE':  'Ireland',
    'IL':  'Israel',
    'IM':  'Isle of Man',
    'IN':  'India',
    'IQ':  'Iraq',
    'IR':  'Iran (Islamic Republic of)',
    'IS':  'Iceland',
    'IT':  'Italy',
    'JE':  'Jersey',
    'JM':  'Jamaica',
    'JO':  'Jordan',
    'JP':  'Japan',
    'KE':  'Kenya',
    'KG':  'Kyrgyzstan',
    'KH':  'Cambodia',
    'KI':  'Kiribati',
    'KM':  'Comoros',
    'KN':  'Saint Kitts and Nevis',
    'KP':  'Korea (Democratic People\'s Republic of)',
    'KR':  'Korea (Republic of)',
    # Page 7
    "KW":  "Kuwait",
    "KY":  "Cayman Islands",
    "KZ":  "Kazakhstan",
    "LA":  "Lao People's Democratic Republic",
    "LB":  "Lebanon",
    "LC":  "Saint Lucia",
    "LI":  "Liechtenstein",
    "LK":  "Sri Lanka",
    "LR":  "Liberia",
    "LS":  "Lesotho",
    "LT":  "Lithuania",
    "LU":  "Luxembourg",
    "LV":  "Latvia",
    "LY":  "Libya",
    "MA":  "Morocco",
    "MC":  "Monaco",
    "MD":  "Moldova, Republic of",
    "ME":  "Montenegro",
    "MF":  "Saint Martin (French part)",
    "MG":  "Madagascar",
    # Page 8
    "MH":  "Marshall Islands",
    "MK":  "North Macedonia",
    "ML":  "Mali",
    "MM":  "Myanmar",
    "MN":  "Mongolia",
    "MO":  "Macao",
    "MP":  "Northern Mariana Islands",
    "MQ":  "Martinique",
    "MR":  "Mauritania",
    "MS":  "Montserrat",
    "MT":  "Malta",
    "MU":  "Mauritius",
    "MV":  "Maldives",
    "MW":  "Malawi",
    "MX":  "Mexico",
    "MY":  "Malaysia",
    "MZ":  "Mozambique",
    "NA":  "Namibia",
    "NC":  "New Caledonia",
    "NE":  "Niger",
    # Page 9
    "NF":  "Norfolk Island",
    "NG":  "Nigeria",
    "NI":  "Nicaragua",
    "NL":  "Netherlands",
    "NO":  "Norway",
    "NP":  "Nepal",
    "NR":  "Nauru",
    "NU":  "Niue",
    "NZ":  "New Zealand",
    "OM":  "Oman",
    "PA":  "Panama",
    "PE":  "Peru",
    "PF":  "French Polynesia",
    "PG":  "Papua New Guinea",
    "PH":  "Philippines",
    "PK":  "Pakistan",
    "PL":  "Poland",
    "PM":  "Saint Pierre and Miquelon",
    "PN":  "Pitcairn",
    "PR":  "Puerto Rico",
    # Page 10
    "PS":  "Palestine, State of",
    "PT":  "Portugal",
    "PW":  "Palau",
    "PY":  "Paraguay",
    "QA":  "Qatar",
    "RE":  "Réunion",
    "RO":  "Romania",
    "RS":  "Serbia",
    "RU":  "Russian Federation",
    "RW":  "Rwanda",
    "SA":  "Saudi Arabia",
    "SB":  "Solomon Islands",
    "SC":  "Seychelles",
    "SD":  "Sudan",
    "SE":  "Sweden",
    "SG":  "Singapore",
    "SH":  "Saint Helena, Ascension and Tristan da Cunha",
    "SI":  "Slovenia",
    "SJ":  "Svalbard and Jan Mayen",
    "SK":  "Slovakia",
    # Page 11
    "SL":  "Sierra Leone",
    "SM":  "San Marino",
    "SN":  "Senegal",
    "SO":  "Somalia",
    "SR":  "Suriname",
    "SS":  "South Sudan",
    "ST":  "São Tomé and Príncipe",
    "SV":  "El Salvador",
    "SX":  "Sint Maarten (Dutch part)",
    "SY":  "Syrian Arab Republic",
    "SZ":  "Eswatini",
    "TC":  "Turks and Caicos Islands",
    "TD":  "Chad",
    "TF":  "French Southern Territories",
    "TG":  "Togo",
    "TH":  "Thailand",
    "TJ":  "Tajikistan",
    "TK":  "Tokelau",
    "TL":  "Timor-Leste",
    "TM":  "Turkmenistan",
    # Page 12
    "TN":  "Tunisia",
    "TO":  "Tonga",
    "TR":  "Türkiye",
    "TT":  "Trinidad and Tobago",
    "TV":  "Tuvalu",
    "TW":  "Taiwan, Province of China",
    "TZ":  "Tanzania, United Republic of",
    "UA":  "Ukraine",
    "UG":  "Uganda",
    "US":  "United States of America",
    "UY":  "Uruguay",
    "UZ":  "Uzbekistan",
    "VA":  "Holy See",
    "VC":  "Saint Vincent and the Grenadines",
    "VE":  "Venezuela, Bolivarian Republic of",
    "VG":  "Virgin Islands (British)",
    "VI":  "Virgin Islands (U.S.)",
    "VN":  "Viet Nam",
    "VU":  "Vanuatu",
    "WF":  "Wallis and Futuna",
    # Page 13
    'WS':  'Samoa',
    'XK':  'Kosovo',
    'YE':  'Yemen',
    'YT':  'Mayotte',
    'ZA':  'South Africa',
    'ZM':  'Zambia',
    'ZW':  'Zimbabwe',
}
# Load data (assuming it's in a JSON file)
with open("cities.sorted.json", "r", encoding="utf-8") as file:
    cities = json.load(file)


def escape_ruby_string(value):
    return value.replace("'", "\\'")


# Step 1: Group by country
country_groups = defaultdict(list)

for city in cities:
    country = city.get("country", "Unknown")
    """
        Append a city object to the list of cities for the country with:
            - name
            - state
            - coord: {lat, lon}
    """
    city.pop("id", None)
    city.update({
        "name": escape_ruby_string(city["name"]),
        "state": escape_ruby_string(city.get("state", "")),
    })
    country_groups[country].append(city)

"""
    Translate and write them into countries/<country>_seeder.rb file in the following format:
    [
        <country> => [
            ...list of cities...
        ]
    ]
"""
# Check if countries directory exists
if not os.path.exists("countries"):
    os.makedirs("countries")
for country, city_list in country_groups.items():
    if country == "":
        country = "Unknown"
    with open(f"countries/{country.lower()}_seeder.rb", "w", encoding="utf-8") as file:
        file.write(f"# {country} cities\n")
        file.write("\n[\n")

        for city in city_list:
            file.write("    {\n")
            file.write(f"        :name => '{city['name']}',\n")
            file.write(f"        :state => '{city['state']}',\n")
            file.write(f"        :country => '{escape_ruby_string(COUNTRY_NAME.get(city['country']))}',\n")
            file.write(f"        :country_code => '{city['country']}',\n")
            file.write(f"        :lat => {city['coord']['lat']},\n")
            file.write(f"        :lon => {city['coord']['lon']},\n")
            file.write("    },\n")
        file.write("];\n")
