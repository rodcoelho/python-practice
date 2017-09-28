import requests
import json
from bs4 import BeautifulSoup

WWOurl = 'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=2070915380d345728e5133011171008&q=37.75,-122.51&format=json&includelocation=yes&tide=yes&tp=6'
key = '2070915380d345728e5133011171008'

r = requests.get(WWOurl)
text = r.json()
#how to get data from variable text
x = text["data"]["request"][0]["query"]
print(x)






decision_question = "Where would you like to surf?"
pickRegion = ('British Columbia', 'Pacific Northwest', 'Northern California', 'Central California',
        'Southern California', 'Eastern Canada', 'Great Lakes', 'New England', 'Long Island',
        'Mid Atlantic', 'Virginia - Outer Banks', 'Southeast', 'Florida' , 'Florida Gulf',
        'Gulf States', 'Texas', 'Kauai', 'Oahu', 'Maui', 'Big Island Hawaii', 'Lanai',
        'Molokai', 'Northern Baja', 'Southern Baja', 'Northern Mexico', 'Southern Mexico'
     )




spotLocation_NorthAmerica = {
    'United States' : {
        'Pacific Northwest': {
            'Alaska': {
                'Fossil Beach': ['http://www.surfline.com/surf-forecasts/spot/fossil-beach_25050/', ],
                'Kodiak Alaska': ['http://www.surfline.com/surf-forecasts/spot/kodiak-alaska_53807/', ],
                'Cannon Beach': ['http://www.surfline.com/surf-forecasts/spot/cannon-beach_25052/', ],
                'The Wall': ['http://www.surfline.com/surf-forecasts/spot/the-wall_25053/', ]
            },
            'Washington': {
                'La Push': ['http://www.surfline.com/surf-forecasts/spot/la-push_5068/', ],
                'Westport': ['http://www.surfline.com/surf-forecasts/spot/westport-olympic-peninsula_5067/', ],
                'Long Beach Peninsula': ['http://www.surfline.com/surf-forecasts/spot/long-beach-peninsula_5066/', ]
            },
            'Oregon': {
                'Seaside': ['http://www.surfline.com/surf-forecasts/spot/seaside_142801/'],
                'The Cove': ['http://www.surfline.com/surf-forecasts/spot/the-cove_110661/'],
                'Indian Beach': ['http://www.surfline.com/surf-forecasts/spot/indian-beach_110659/'],
                'Cannon Beach': ['http://www.surfline.com/surf-forecasts/spot/cannon-beach_5077/'],
                'Short Sands':['http://www.surfline.com/surf-forecasts/spot/short-sands_110660/'],
                'Manzanita':['http://www.surfline.com/surf-forecasts/spot/manzanita_142795/'],
                'Rockaway Beach':['http://www.surfline.com/surf-forecasts/spot/rockaway-beach_5076/'],
                'Oceanside Oregon':['http://www.surfline.com/surf-forecasts/spot/oceanside-or_47668/'],
                'Pacific City':['http://www.surfline.com/surf-forecasts/spot/pacific-city_5075/'],
                'Roads End':['http://www.surfline.com/surf-forecasts/spot/roads-end_4186/'],
                'Lincoln City':['http://www.surfline.com/surf-forecasts/spot/lincoln-city_5074/'],
                'Beveryly Beach': ['http://www.surfline.com/surf-forecasts/spot/beverly-beach_142796/'],
                'Agate Beach':['http://www.surfline.com/surf-forecasts/spot/agate-beach_142797/'],
                'Newport':['http://www.surfline.com/surf-forecasts/spot/newport_5073/'],
                'Florence South Jetty':['http://www.surfline.com/surf-forecasts/spot/florence-south-jetty_5072/'],
                'Port Orford':['http://www.surfline.com/surf-forecasts/spot/port-orford_5071/'],
                'Gold Beach': ['http://www.surfline.com/surf-forecasts/spot/gold-beach-south-jetty_5070/'],
                'Brookings Jetty': ['http://www.surfline.com/surf-forecasts/spot/brookings-jetty_5069/']
            }
        },
        'Northern California': {
            'Humboldt': {
                'South Beach': ['http://www.surfline.com/surf-forecasts/spot/south-beach-ca_5088/'],
                'Patricks Point': ['http://www.surfline.com/surf-forecasts/spot/patricks-point_5087/'],
                'Westhaven': ['http://www.surfline.com/surf-forecasts/spot/westhaven_5086/'],
                'Humboldt Harbor Entrance': ['http://www.surfline.com/surf-forecasts/spot/humboldt-harbor-entrance_5084/'],
                'North Jetty': ['http://www.surfline.com/surf-forecasts/spot/north-jetty_5085/'],
                'Shelter Cove': ['http://www.surfline.com/surf-forecasts/spot/shelter-cove_5083/'],
                'SE Papa': ['http://www.surfline.com/surf-forecasts/spot/se-papa_39047/']
            },
            'Mendocino': {
                'Westport': ['http://www.surfline.com/surf-forecasts/spot/westport_5542/'],
                'MacKerricher': ['http://www.surfline.com/surf-forecasts/spot/mackerricher_5543/'],
                'Caspar Beach' : ['http://www.surfline.com/surf-forecasts/spot/caspar-beach_95156/'],
                'Mendocino Township': ['http://www.surfline.com/surf-forecasts/spot/mendocino-township_5544/'],
                'Point Arena': ['http://www.surfline.com/surf-forecasts/spot/point-arena_5545/']
            },
            'Sonoma County': {
                'Black Point Beach': ['http://www.surfline.com/surf-forecasts/spot/black-point-beach_5098/'],
                'Russian Rivermouth': ['http://www.surfline.com/surf-forecasts/spot/russian-rivermouth_5097/'],
                'Salmon Creek': ['http://www.surfline.com/surf-forecasts/spot/salmon-creek_5096/'],
                'Doran Beach': ['http://www.surfline.com/surf-forecasts/spot/doran-beach_5095/']
            },
            'Marin': {
                'Dillon Beach' : ['http://www.surfline.com/surf-forecasts/spot/dillon-beach_64347/'],
                'Point Reyes North' : ['http://www.surfline.com/surf-forecasts/spot/point-reyes-north_5093/'],
                'Bolinas Jetty' : ['http://www.surfline.com/surf-forecasts/spot/bolinas-jetty_5091/'],
                'Stinson Beach' : ['http://www.surfline.com/surf-forecasts/spot/stinson-beach_5090/'],
                'Fort Cronkite, Rodeo Beach' : ['http://www.surfline.com/surf-forecasts/spot/fort-cronkite-rodeo-beach_5089/']
            },
            'SF-San Mateo County': {
                'Fort Point': ['http://www.surfline.com/surf-forecasts/spot/fort-point_5015/'],
                'Ocean Beach SF': ['http://www.surfline.com/surf-forecasts/spot/ocean-beach-overview_4127/'],
                'Central Ocean Beach North': ['http://www.surfline.com/surf-forecasts/spot/central-ocean-beach-north_145752/'],
                'Central Ocean Beach South': ['http://www.surfline.com/surf-forecasts/spot/central-ocean-beach-south_145753/'],
                'South Ocean Beach': ['http://www.surfline.com/surf-forecasts/spot/south-ocean-beach_4128/'],
                'Sharp Park': ['http://www.surfline.com/surf-forecasts/spot/sharp-park_5017/'],
                'Rockaway': ['http://www.surfline.com/surf-forecasts/spot/rockaway_5014/'],
                'Pacifica, Lindamar': ['http://www.surfline.com/surf-forecasts/spot/pacifica-lindamar_5013/'],
                'Pedro Point': ['http://www.surfline.com/surf-forecasts/spot/pacifica-lindamar_5013/'],
                'Montara': ['http://www.surfline.com/surf-forecasts/spot/montara_5011/'],
                'Mavericks': ['http://www.surfline.com/surf-forecasts/spot/mavericks_4152/'],
                'Princeton Jetty': ['http://www.surfline.com/surf-forecasts/spot/princeton-jetty_5008/'],
                'Half Moon Bay': ['http://www.surfline.com/surf-forecasts/spot/half-moon-bay_5007/'],
                'Tunitas Creek': ['http://www.surfline.com/surf-forecasts/spot/tunitas-creek_5005/'],
                'Pescadero': ['http://www.surfline.com/surf-forecasts/spot/pescadero_5018/'],
                'Pigeon Point': ['http://www.surfline.com/surf-forecasts/spot/pigeon-point_5019/'],
                'Ano Nuevo': ['http://www.surfline.com/surf-forecasts/spot/ano-nuevo_5020/']
            }
        },

        'Central California': {
            'Santa Cruz': {
                'Waddell' : ['http://www.surfline.com/surf-forecasts/spot/waddell-creek_5021/', '37.09,-122.27'],
                'Scott Creek': ['http://www.surfline.com/surf-forecasts/spot/scott-creek_5022/'],
                'Davenport': ['http://www.surfline.com/surf-forecasts/spot/davenport_5024/'],
                'Four Mile': ['http://www.surfline.com/surf-forecasts/spot/four-mile_5023/'],
                'Natural Bridges': ['http://www.surfline.com/surf-forecasts/spot/natural-bridges_5027/'],
                'Mitchell Cove': ['http://www.surfline.com/surf-forecasts/spot/mitchells-cove_5028/'],
                'Steamer Lane': ['http://www.surfline.com/surf-forecasts/spot/steamer-lane-overview_4188/'],
                'Steamer Lane Fixed': ['http://www.surfline.com/surf-forecasts/spot/steamer-lane_132587/'],
                'Cowells': ['http://www.surfline.com/surf-forecasts/spot/cowells_4189/'],
                'Cowells Overview': ['http://www.surfline.com/surf-forecasts/spot/cowells-overview_140552/'],
                'The Harbor': ['http://www.surfline.com/surf-forecasts/spot/the-harbor_5031/'],
                '26th Ave': ['http://www.surfline.com/surf-forecasts/spot/26th-ave_5030/'],
                'Pleasure Point': ['http://www.surfline.com/surf-forecasts/spot/pleasure-point_4190/'],
                '38th Ave': ['http://www.surfline.com/surf-forecasts/spot/jacks_4191/'],
                'Capitola': ['http://www.surfline.com/surf-forecasts/spot/capitola_10763/'],
                'Manresa': ['http://www.surfline.com/surf-forecasts/spot/manresa_5036/'],
                'The Hook': ['http://www.surfline.com/surf-forecasts/spot/the-hook_108024/']
            },
            'Monterey':{
                'Moss Landing': ['http://www.surfline.com/surf-forecasts/spot/moss-landing_6063/'],
                'Marina State Beach': ['http://www.surfline.com/surf-forecasts/spot/marina-state-beach_4957/'],
                'Monterey State Beach': ['http://www.surfline.com/surf-forecasts/spot/monterey-state-beach_140547/'],
                'Monterey Bay': ['http://www.surfline.com/surf-forecasts/spot/monterey-bay_135849/'],
                'Lovers Point': ['http://www.surfline.com/surf-forecasts/spot/lovers-point_6008/'],
                'Boneyard': ['http://www.surfline.com/surf-forecasts/spot/boneyard_6006/'],
                'Asilomar': ['http://www.surfline.com/surf-forecasts/spot/asilomar_6009/'],
                'Mole Point': ['http://www.surfline.com/surf-forecasts/spot/mole-point_6007/'],
                'Ghost Tree': ['http://www.surfline.com/surf-forecasts/spot/ghost-tree_6059/'],
                'Carmel Beach': ['http://www.surfline.com/surf-forecasts/spot/carmel-beach_6003/'],
                'Big Sur Rivermouth': ['http://www.surfline.com/surf-forecasts/spot/big-sur-rivermouth_6005/'],
                'Sand Dollar Beach': ['http://www.surfline.com/surf-forecasts/spot/sand-dollar-beach_6002/'],
                'Willow Creek': ['http://www.surfline.com/surf-forecasts/spot/willow-creek_6010/']
            },
            'San Luis Obispo County': {
                'Piedras Biancas': ['http://www.surfline.com/surf-forecasts/spot/piedras-blancas_135851/'],
                'Pico Creek': ['http://www.surfline.com/surf-forecasts/spot/pico-creek_5053/'],
                'San Simeon': ['http://www.surfline.com/surf-forecasts/spot/san-simeon_5051/'],
                'Moonstone': ['http://www.surfline.com/surf-forecasts/spot/moonstone_5054/'],
                'Santa Rosa Creek': ['http://www.surfline.com/surf-forecasts/spot/santa-rosa-creek_5055/'],
                'Cayucos Pier': ['http://www.surfline.com/surf-forecasts/spot/cayucos-pier_5057/'],
                'Cayucos Overview': ['http://www.surfline.com/surf-forecasts/spot/cayucos-overview_135838/'],
                'Morro Bay North': ['http://www.surfline.com/surf-forecasts/spot/morro-bay-north_135840/'],
                'Morro Bay': ['http://www.surfline.com/surf-forecasts/spot/morro-bay_4193/'],
                'Morro Bay Harbor Entrace': ['http://www.surfline.com/surf-forecasts/spot/morro-bay-harbor-entrance_136184/'],
                'Morro Bay Harbor': ['http://www.surfline.com/surf-forecasts/spot/morro-bay-harbor_135841/'],
                'Morro Bay Boat Launch': ['http://www.surfline.com/surf-forecasts/spot/morro-bay-boat-launch_138701/'],
                'Morro Bay Overview': ['http://www.surfline.com/surf-forecasts/spot/morro-bay-overview_140404/'],
                'Baywood Beach': ['http://www.surfline.com/surf-forecasts/spot/baywood-beach_135850/'],
                'Cable Landing': ['http://www.surfline.com/surf-forecasts/spot/cable-landing_5060/'],
                'Avila Beach': ['http://www.surfline.com/surf-forecasts/spot/avila-beach_5064/'],
                'Shell Beach': ['http://www.surfline.com/surf-forecasts/spot/shell-beach_66211/'],
                'Shell Beach South': ['http://www.surfline.com/surf-forecasts/spot/shell-beach-south_136964/'],
                'Shell Beach Overview': ['http://www.surfline.com/surf-forecasts/spot/shell-beach-overview_136965/'],
                'Pismo Beach North': ['http://www.surfline.com/surf-forecasts/spot/pismo-beach-north_135842/'],
                'Pismo Beach Pier': ['http://www.surfline.com/surf-forecasts/spot/pismo-beach-pier_5065/'],
                'Pismo Beach South': ['http://www.surfline.com/surf-forecasts/spot/pismo-beach-south_135843/'],
                'Oceano, Pier Ave': ['http://www.surfline.com/surf-forecasts/spot/oceano-pier-ave_146037/'],
                'Oceano': ['http://www.surfline.com/surf-forecasts/spot/oceano_135852/']
            }
        },
        'Southern California': {
            'North Santa Barbara County': {
                'Surf Beach': ['http://www.surfline.com/surf-forecasts/spot/surf-beach_5043/'],
                'Jalama': ['http://www.surfline.com/surf-forecasts/spot/jalama_5038/'],
                'Point Conception': ['http://www.surfline.com/surf-forecasts/spot/point-conception_5039/']
            },
            'Santa Barbara': {
                'Refugio': ['http://www.surfline.com/surf-forecasts/spot/refugio_4991/'],
                'El Capitan': ['http://www.surfline.com/surf-forecasts/spot/el-capitan_4993/'],
                'Sands': ['http://www.surfline.com/surf-forecasts/spot/sands_4994/'],
                'Coal Oil Point': ['http://www.surfline.com/surf-forecasts/spot/coal-oil-point_4995/'],
                'Campus Point': ['http://www.surfline.com/surf-forecasts/spot/campus-point_4997/'],
                'Leadbetter Beach': ['http://www.surfline.com/surf-forecasts/spot/leadbetter-beach_145542/'],
                'Leadbetter Point': ['http://www.surfline.com/surf-forecasts/spot/leadbetter-point_4990/'],
                'Sandspit': ['http://www.surfline.com/surf-forecasts/spot/sandspit_4998/'],
                'Santa Barbara Harbor': ['http://www.surfline.com/surf-forecasts/spot/santa-barbara-harbor-overview_139341/'],
                'Hammonds': ['http://www.surfline.com/surf-forecasts/spot/hammonds_4999/'],
                'Carpinteria State Beach': ['http://www.surfline.com/surf-forecasts/spot/carpinteria-state-beach_5001/'],
                'Tarpits': ['http://www.surfline.com/surf-forecasts/spot/tarpits_5000/'],
                'Rincon': ['http://www.surfline.com/surf-forecasts/spot/rincon_4197/']
            },
            'Ventura': {
                'Mussel Shoals, Little Rincon': ['http://www.surfline.com/surf-forecasts/spot/mussel-shoals-aka-little-rincon_4985/'],
                'Oil Piers': ['http://www.surfline.com/surf-forecasts/spot/oil-piers_4961/'],
                'Stanleys': ['http://www.surfline.com/surf-forecasts/spot/stanleys_4960/'],
                'Pitas Point': ['http://www.surfline.com/surf-forecasts/spot/pitas-point_4981/'],
                'Mondos': ['http://www.surfline.com/surf-forecasts/spot/mondos_49737/'],
                'Solimar': ['http://www.surfline.com/surf-forecasts/spot/solimar_4989/'],
                'Gold Coast Beachbreaks': ['http://www.surfline.com/surf-forecasts/spot/gold-coast-beachbreaks_4198/'],
                'Summer Beach': ['http://www.surfline.com/surf-forecasts/spot/summer-beach_4988/'],
                'Emma Wood': ['http://www.surfline.com/surf-forecasts/spot/emma-wood_4980/'],
                'Ventura Overhead': ['http://www.surfline.com/surf-forecasts/spot/ventura-overhead_4982/'],
                'Ventura Point': ['http://www.surfline.com/surf-forecasts/spot/ventura-point_89981/'],
                'C Street': ['http://www.surfline.com/surf-forecasts/spot/c-st_4200/'],
                'C Street Fixed': ['http://www.surfline.com/surf-forecasts/spot/c-st-overview_135844/'],
                'Ventura Harbor': ['http://www.surfline.com/surf-forecasts/spot/ventura-harbor_4201/'],
                'Oxnard': ['http://www.surfline.com/surf-forecasts/spot/oxnard_4968/']
            },
            'North Los Angeles': {
                'Country Line': ['http://www.surfline.com/surf-forecasts/spot/county-line_4203/'],
                'Country Line Overview': ['http://www.surfline.com/surf-forecasts/spot/county-line-overview_135846/'],
                'Leo Carrillo': ['http://www.surfline.com/surf-forecasts/spot/leo-carrillo_4953/'],
                'Zuma': ['http://www.surfline.com/surf-forecasts/spot/zuma_4949/'],
                'Point Dume': ['http://www.surfline.com/surf-forecasts/spot/point-dume_4947/'],
                'Latigo Point': ['http://www.surfline.com/surf-forecasts/spot/latigo-point_4944/'],
                'Malibu': ['http://www.surfline.com/surf-forecasts/spot/malibu-second-to-third-point_4209/'],
                'Malibu First Point': ['http://www.surfline.com/surf-forecasts/spot/malibu-first-point_119811/'],
                'Malibu Overview': ['http://www.surfline.com/surf-forecasts/spot/malibu-overview_135847/'],
                'Topanga': ['http://www.surfline.com/surf-forecasts/spot/topanga-beach_4210/'],
                'Topanga Beach OVerview': ['http://www.surfline.com/surf-forecasts/spot/topanga-beach-overview_146345/'],
                'Chart House': ['http://www.surfline.com/surf-forecasts/spot/chart-house_4940/'],
                'Sunset Point': ['http://www.surfline.com/surf-forecasts/spot/sunset-point_4883/'],
                'Sunset Beach': ['http://www.surfline.com/surf-forecasts/spot/sunset-beach_119813/']
            },
            'South Los Angeles': {
                'Santa Monica Pier': ['http://www.surfline.com/surf-forecasts/spot/santa-monica-pier_4886/'],
                'Venice Beach': ['http://www.surfline.com/surf-forecasts/spot/venice-beach_4211/'],
                'Venice Breakwater': ['http://www.surfline.com/surf-forecasts/spot/venice-breakwater_146850/'],
                'DockWeiler State Beach': ['http://www.surfline.com/surf-forecasts/spot/dockweiler-state-beach_4895/'],
                'Shitpipe': ['http://www.surfline.com/surf-forecasts/spot/shitpipe_4896/'],
                'El Porto North': ['http://www.surfline.com/surf-forecasts/spot/el-porto-north_142785/'],
                'El Porto': ['http://www.surfline.com/surf-forecasts/spot/el-porto_4900/'],
                'Manhattan Beach': ['http://www.surfline.com/surf-forecasts/spot/manhattan-beach_4901/'],
                'Hermosa Beach': ['http://www.surfline.com/surf-forecasts/spot/hermosa-beach_4902/'],
                'Redondo Breakwater': ['http://www.surfline.com/surf-forecasts/spot/redondo-breakwater_4912/'],
                'Redondo Jetty': ['http://www.surfline.com/surf-forecasts/spot/sapphire-st_139023/'],
                'Torrance Beach, Haggertys': ['http://www.surfline.com/surf-forecasts/spot/torrance-beach-to-haggertys_4910/'],
                'PV Cove': ['http://www.surfline.com/surf-forecasts/spot/pv-cove_4936/'],
                'Lunada Bay': ['http://www.surfline.com/surf-forecasts/spot/lunada-bay_4935/'],
                'Cabrillo Beach': ['http://www.surfline.com/surf-forecasts/spot/cabrillo-beach_4931/']
            },
            'North Orange County': {
                'Seal Beach Overview': ['http://www.surfline.com/surf-forecasts/spot/seal-beach-overview_4217/'],
                'South Side, 13th Street': ['http://www.surfline.com/surf-forecasts/spot/south-side-13th-street_4865/'],
                'Surfside': ['http://www.surfline.com/surf-forecasts/spot/surfside_4867/'],
                'Anderson Street': ['http://www.surfline.com/surf-forecasts/spot/anderson-st_4219/'],
                'Bolsa Chica State North': ['http://www.surfline.com/surf-forecasts/spot/bolsa-chica-state-beach-n_145499/'],
                'Bolsa Chica Overview': ['http://www.surfline.com/surf-forecasts/spot/bolsa-chica-overview_103685/'],
                'Goldenwest': ['http://www.surfline.com/surf-forecasts/spot/goldenwest_4870/'],
                '17th Street': ['http://www.surfline.com/surf-forecasts/spot/17th-st_4871/'],
                'HB Pier, Northside Overview': ['http://www.surfline.com/surf-forecasts/spot/hb-pier-northside-overview_58218/'],
                'HB Pier, Northside': ['http://www.surfline.com/surf-forecasts/spot/hb-pier-northside_4223/'],
                'HB Pier, Southside': ['http://www.surfline.com/surf-forecasts/spot/hb-pier-southside_4874/'],
                'HB Pier South Closeup': ['http://www.surfline.com/surf-forecasts/spot/hb-pier-south-closeup_148545/'],
                'HB Pier, Southside Overview': ['http://www.surfline.com/surf-forecasts/spot/hb-pier-southside-overview_144645/'],
                'Huntington St. Overview': ['http://www.surfline.com/surf-forecasts/spot/huntington-st-overview_144646/'],
                'Huntington State Beach': ['http://www.surfline.com/surf-forecasts/spot/huntington-state-beach_103681/'],
                'Santa Ana River Jetties': ['http://www.surfline.com/surf-forecasts/spot/santa-ana-river-jetties_4875/'],
                '56th Street': ['http://www.surfline.com/surf-forecasts/spot/56th-st_43103/'],
                '54th Street': ['http://www.surfline.com/surf-forecasts/spot/54th-st_130559/'],
                'Newport Jetties': ['http://www.surfline.com/surf-forecasts/spot/newport-jetties_4876/'],
                '40 Street Newport': ['http://www.surfline.com/surf-forecasts/spot/40-st-newport_4225/'],
                '36th Street': ['http://www.surfline.com/surf-forecasts/spot/36th-st_4226/'],
                'Lower Jetties': ['http://www.surfline.com/surf-forecasts/spot/lower-jetties_131676/'],
                'Blackies': ['http://www.surfline.com/surf-forecasts/spot/blackies_53412/'],
                'Newport Beach Pier': ['http://www.surfline.com/surf-forecasts/spot/newport-beach-pier_4227/'],
                'Newport Point': ['http://www.surfline.com/surf-forecasts/spot/newport-point_4877/'],
                'The Wedge': ['http://www.surfline.com/surf-forecasts/spot/the-wedge_4232/'],
                'Corona del Mar': ['http://www.surfline.com/surf-forecasts/spot/corona-del-mar_4879/'],
                'Crystal Cove': ['http://www.surfline.com/surf-forecasts/spot/crystal-cove_46525/']
            },
            'South Orange County': {
                'Rockpile': ['http://www.surfline.com/surf-forecasts/spot/rockpile_4860/'],
                'Thalia Street': ['http://www.surfline.com/surf-forecasts/spot/thalia-street_4857/'],
                'Brooks Street': ['http://www.surfline.com/surf-forecasts/spot/brooks-street_4856/'],
                'Aliso Creek': ['http://www.surfline.com/surf-forecasts/spot/aliso-creek_4855/'],
                'Salt Creek': ['http://www.surfline.com/surf-forecasts/spot/salt-creek_4233/'],
                'Strands': ['http://www.surfline.com/surf-forecasts/spot/strands_4849/'],
                'Boneyard': ['http://www.surfline.com/surf-forecasts/spot/boneyard_145717/'],
                'Doheny Rivermouth': ['http://www.surfline.com/surf-forecasts/spot/doheny-rivermouth_145718/'],
                'Doheny State Beach': ['http://www.surfline.com/surf-forecasts/spot/doheny-state-beach_4848/'],
                'T Street': ['http://www.surfline.com/surf-forecasts/spot/t-street_4235/'],
                'San Clemente State Beach': ['http://www.surfline.com/surf-forecasts/spot/san-clemente-state-beach_4843/'],
                'Cottons': ['http://www.surfline.com/surf-forecasts/spot/cottons_4737/'],
                'Upper Trestles': ['http://www.surfline.com/surf-forecasts/spot/upper-trestles_4738/'],
                'Lower Trestles' : ['http://www.surfline.com/surf-forecasts/spot/lower-trestles_4740/'],
                'Middles': ['http://www.surfline.com/surf-forecasts/spot/middles_4739/'],
                'Church': ['http://www.surfline.com/surf-forecasts/spot/church_4741/'],
                'The Point at San Onofre': ['http://www.surfline.com/surf-forecasts/spot/the-point-at-san-onofre_4237/'],
                'Old Mans at San Onofre': ['http://www.surfline.com/surf-forecasts/spot/old-mans-at-san-onofre_109918/'],
                'Trails': ['http://www.surfline.com/surf-forecasts/spot/trails_4736/']
            },
            'North San Diego': {
                'Oceanside Harbor': ['http://www.surfline.com/surf-forecasts/spot/oceanside-harbor_4238/'],
                'Oceanside Pier, Northside': ['http://www.surfline.com/surf-forecasts/spot/oceanside-pier-northside_4241/'],
                'Oceanside Pier, Southside': ['http://www.surfline.com/surf-forecasts/spot/oceanside-pier-southside_68366/'],
                'Tamarack': ['http://www.surfline.com/surf-forecasts/spot/tamarack_4242/'],
                'Terra Mar Point': ['http://www.surfline.com/surf-forecasts/spot/terra-mar-point_4775/'],
                'Ponto North': ['http://www.surfline.com/surf-forecasts/spot/ponto-north_128083/'],
                'Ponto Jetties': ['http://www.surfline.com/surf-forecasts/spot/ponto-jetties_4773/'],
                'Grandview': ['http://www.surfline.com/surf-forecasts/spot/grandview_4771/'],
                'Beacons': ['http://www.surfline.com/surf-forecasts/spot/beacons_4772/'],
                'Moonlight Beach': ['http://www.surfline.com/surf-forecasts/spot/moonlight-beach_4770/'],
                'D Street': ['http://www.surfline.com/surf-forecasts/spot/d-street_4792/'],
                'Swamis': ['http://www.surfline.com/surf-forecasts/spot/swamis_4789/'],
                'Pipes': ['http://www.surfline.com/surf-forecasts/spot/pipes_4790/'],
                'San Elijo State Beach': ['http://www.surfline.com/surf-forecasts/spot/san-elijo-campground-overview_4791/'],
                'Cardiff': ['http://www.surfline.com/surf-forecasts/spot/cardiff-reef-overview_4786/'],
                'Cardiff Reef': ['http://www.surfline.com/surf-forecasts/spot/cardiff-reef-south_139590/'],
                'Georges': ['http://www.surfline.com/surf-forecasts/spot/georges_139591/'],
                'Seaside Reef': ['http://www.surfline.com/surf-forecasts/spot/seaside-reef_4787/'],
                'Del Mar Rivermouth': ['http://www.surfline.com/surf-forecasts/spot/del-mar-rivermouth_4785/'],
                'Del Mar 25th Street': ['http://www.surfline.com/surf-forecasts/spot/25th-st_139340/'],
                'Del Mar Beachbreak': ['http://www.surfline.com/surf-forecasts/spot/del-mar-beachbreak_4784/'],
                'Del Mar': ['http://www.surfline.com/surf-forecasts/spot/15th-to-18th-st_4783/']
            },
            'South San Diego': {
                'Torrey Pines State': ['http://www.surfline.com/surf-forecasts/spot/torrey-pines-state-beach-s_107951/'],
                'Blacks': ['http://www.surfline.com/surf-forecasts/spot/blacks_4245/'],
                'Scripps': ['http://www.surfline.com/surf-forecasts/spot/scripps_4246/'],
                'La Jolla Shores': ['http://www.surfline.com/surf-forecasts/spot/la-jolla-shores_4812/'],
                'Horseshoe': ['http://www.surfline.com/surf-forecasts/spot/horseshoe_4247/'],
                'Windansea': ['http://www.surfline.com/surf-forecasts/spot/windansea_4248/'],
                'Birdrock': ['http://www.surfline.com/surf-forecasts/spot/birdrock_4249/'],
                'PB Point': ['http://www.surfline.com/surf-forecasts/spot/pb-point_4803/'],
                'Old Mans at Tourmaline': ['http://www.surfline.com/surf-forecasts/spot/old-mans-at-tourmaline_4804/'],
                'Pacific Beach': ['http://www.surfline.com/surf-forecasts/spot/pacific-beach_4250/'],
                'Mission Beach': ['http://www.surfline.com/surf-forecasts/spot/mission-beach_4252/'],
                'Ocean Beach, SD': ['http://www.surfline.com/surf-forecasts/spot/ocean-beach_4253/'],
                'Sunset Cliffs': ['http://www.surfline.com/surf-forecasts/spot/sunset-cliffs_4254/'],
                'Coronado Beach': ['http://www.surfline.com/surf-forecasts/spot/coronado-beach_4816/'],
                'Imperial Pier NS': ['http://www.surfline.com/surf-forecasts/spot/imperial-pier-northside_4255/'],
                'Imperial Pier SS': ['http://www.surfline.com/surf-forecasts/spot/imperial-pier-southside_4256/'],
                'Tijuana Slough': ['http://www.surfline.com/surf-forecasts/spot/tijuana-slough_4814/']
            }
            }
        },
        'New England': {
            'New Hampshire - Maine': {
                'Acadia National': ['http://www.surfline.com/surf-forecasts/spot/acadia-national-park_110639/'],
                'Popham Beach': ['http://www.surfline.com/surf-forecasts/spot/popham-beach_110167/'],
                'Higgins Beach': ['http://www.surfline.com/surf-forecasts/spot/higgins-beach_5123/'],
                'Scarborough Beach': ['http://www.surfline.com/surf-forecasts/spot/scarborough-beach-park_5126/'],
                'Old Orchard Beach': ['http://www.surfline.com/surf-forecasts/spot/old-orchard-beach_5127/'],
                'Fortunes Rock': ['http://www.surfline.com/surf-forecasts/spot/fortunes-rock_127818/'],
                'Goochs Beach': ['http://www.surfline.com/surf-forecasts/spot/goochs-beach_5125/'],
                'Wells Beach': ['http://www.surfline.com/surf-forecasts/spot/wells-beach_5124/'],
                'Ogunquit': ['http://www.surfline.com/surf-forecasts/spot/ogunquit_5105/'],
                'York Beach': ['http://www.surfline.com/surf-forecasts/spot/york-beach_146849/'],
                'Short Sands Beach': ['http://www.surfline.com/surf-forecasts/spot/short-sands-beach_5106/'],
                'Long Sands Beach': ['http://www.surfline.com/surf-forecasts/spot/long-sands-beach_5129/'],
                'Straws Point': ['http://www.surfline.com/surf-forecasts/spot/straws-point_5117/'],
                'Sawyers Beach':['http://www.surfline.com/surf-forecasts/spot/sawyers-beach_5122/'],
                'Rye on the Rocks / 5-0': ['http://www.surfline.com/surf-forecasts/spot/rye-on-the-rocks---5-0s_5121/'],
                'Fox Hill': ['http://www.surfline.com/surf-forecasts/spot/fox-hill_5116/'],
                'Plaice Cove': ['http://www.surfline.com/surf-forecasts/spot/plaice-cove_5118/'],
                'The Main Beach': ['http://www.surfline.com/surf-forecasts/spot/the-main-beach_5120/'],
                'The Wall, Hampton Beach': ['http://www.surfline.com/surf-forecasts/spot/the-wall_5131/'],
                'Seabrook': ['http://www.surfline.com/surf-forecasts/spot/seabrook_4263/']
            },
            'Massachursetts': {
                'Nantasket Beach': ['http://www.surfline.com/surf-forecasts/spot/nantasket-beach_5114/'],
                'Egypt Beach' : ['http://www.surfline.com/surf-forecasts/spot/egypt-beach_5113/']
            },
            'Cape Cod': {
                'Marconi Beach': ['http://www.surfline.com/surf-forecasts/spot/marconi-beach_108234/'],
                'Nauset Light Beach': ['http://www.surfline.com/surf-forecasts/spot/nauset-light-beach_108229/'],
                'Coast Guard Beach': ['http://www.surfline.com/surf-forecasts/spot/coast-guard-beach_108228/'],
                'Nauset Beach': ['http://www.surfline.com/surf-forecasts/spot/nauset-beach_108230/'],
                'Cape Cod': ['http://www.surfline.com/surf-forecasts/spot/cape-cod_5115/'],
                'Nantucket' : ['http://www.surfline.com/surf-forecasts/spot/nantucket_30174/'],
                'Marthas Vineyard': ['http://www.surfline.com/surf-forecasts/spot/marthas-vineyard_30239/']
            },
            'Rhode Island': {
                'First Beach': ['http://www.surfline.com/surf-forecasts/spot/first-beach_5111/'],
                'Second Beach': ['http://www.surfline.com/surf-forecasts/spot/second-beach_5112/'],
                'Ruggles - Newport' : ['http://www.surfline.com/surf-forecasts/spot/ruggles---newport_5110/'],
                'Narragansett': ['http://www.surfline.com/surf-forecasts/spot/narragansett_4266/'],
                'Monahans - Narragansett': ['http://www.surfline.com/surf-forecasts/spot/monahans---narragansett_5108/'],
                'Point Judith North': ['http://www.surfline.com/surf-forecasts/spot/point-judith-north_143998/'],
                'Point Judith': ['http://www.surfline.com/surf-forecasts/spot/point-judith_5107/'],
                'Matunuck': ['http://www.surfline.com/surf-forecasts/spot/matunuck_41373/'],
                'Misquamicut State Beach': ['http://www.surfline.com/surf-forecasts/spot/misquamicut-state-beach_9858/']
            }
        },
        'Long Island': {
            'Suffolk County': {
                'Ditch Plains': ['http://www.surfline.com/surf-forecasts/spot/ditch-plains_5142/'],
                'Poles': ['http://www.surfline.com/surf-forecasts/spot/poles_5146/'],
                'Trailer Park': ['http://www.surfline.com/surf-forecasts/spot/trailer-park_5141/'],
                'Terrace': ['http://www.surfline.com/surf-forecasts/spot/terrace_5148/'],
                'Montauk': ['http://www.surfline.com/surf-forecasts/spot/montauk_4268/'],
                'Main Beach': ['http://www.surfline.com/surf-forecasts/spot/main-beach_5147/'],
                'East Hampton Beach': ['http://www.surfline.com/surf-forecasts/spot/east-hampton-beach_77839/'],
                'Coopers Beach' : ['http://www.surfline.com/surf-forecasts/spot/coopers-beach_68789/'],
                'Flys': ['http://www.surfline.com/surf-forecasts/spot/flys_5140/'],
                'The Bowl': ['http://www.surfline.com/surf-forecasts/spot/the-bowl_5139/'],
                'K Road':['http://www.surfline.com/surf-forecasts/spot/k-road_5149/'],
                'Dune Road West': ['http://www.surfline.com/surf-forecasts/spot/dune-rd-west_137585/'],
                'Cupsogue': ['http://www.surfline.com/surf-forecasts/spot/cupsogue_5138/'],
                'Davis Park': ['http://www.surfline.com/surf-forecasts/spot/davis-park-surf_147875/'],
                'Davis Park Marina': ['http://www.surfline.com/surf-forecasts/spot/davis-park-marina_147874/'],
                'Davis Park Beach': ['http://www.surfline.com/surf-forecasts/spot/davis-park-beach_147873/'],
                'Fire Island': ['http://www.surfline.com/surf-forecasts/spot/fire-island_5137/'],
                'Robert Moses': ['http://www.surfline.com/surf-forecasts/spot/robert-moses_5136/'],
                'Gilgo Beach': ['http://www.surfline.com/surf-forecasts/spot/gilgo-beach_5135/']
            },
            'Nassau - Queens County': {
                'West End': ['http://www.surfline.com/surf-forecasts/spot/west-end_5144/'],
                'Lido Beach': ['http://www.surfline.com/surf-forecasts/spot/lido-beach_5132/'],
                'Pacific Blvd': ['http://www.surfline.com/surf-forecasts/spot/pacific-blvd_146186/'],
                'Lincoln Blvd. Fixed': ['http://www.surfline.com/surf-forecasts/spot/lincoln-blvd-overview_5133/'],
                'Lincoln Blvd, Long Beach': ['http://www.surfline.com/surf-forecasts/spot/lincoln-blvd_4269/'],
                'Laurelton Blvd': ['http://www.surfline.com/surf-forecasts/spot/laurelton-blvd_5150/'],
                'West End, Long Beach': ['http://www.surfline.com/surf-forecasts/spot/west-end-long-beach_142784/'],
                '30th - 39th Streets': ['http://www.surfline.com/surf-forecasts/spot/30th---39th-streets_5151/'],
                'Rockaway Beach 77th': ['http://www.surfline.com/surf-forecasts/spot/77th-st-rockaways_137586/'],
                '84th Street': ['http://www.surfline.com/surf-forecasts/spot/84th-street_5152/'],
                'Rockaway Beach 90th': ['http://www.surfline.com/surf-forecasts/spot/90th-st-rockaways_4270/'],
                'Breezy Point': ['http://www.surfline.com/surf-forecasts/spot/breezy-point_5154/']
            }
        },
        'Mid Atlantic': {
            'New Jersey': {
                'Sandy Hook': ['http://www.surfline.com/surf-forecasts/spot/sandy-hook_5164/'],
                'Monmouth': ['http://www.surfline.com/surf-forecasts/spot/monmouth_5163/'],
                'Monmouth Beach': ['http://www.surfline.com/surf-forecasts/spot/monmouth-beach_4276/'],
                'Loch Arbor and Deal': ['http://www.surfline.com/surf-forecasts/spot/loch-arbor-and-deal_5162/'],
                'Asbury Park': ['http://www.surfline.com/surf-forecasts/spot/asbury-park_5161/'],
                'Ocean Grove': ['http://www.surfline.com/surf-forecasts/spot/ocean-grove_5160/'],
                'Bradley Beach': ['http://www.surfline.com/surf-forecasts/spot/bradley-beach_5159/'],
                'Avon': ['http://www.surfline.com/surf-forecasts/spot/avon_5158/'],
                '16th Ave': ['http://www.surfline.com/surf-forecasts/spot/16th-ave_5157/'],
                'Spring Lake': ['http://www.surfline.com/surf-forecasts/spot/spring-lake_5156/'],
                'Sea Girt': ['http://www.surfline.com/surf-forecasts/spot/sea-girt_5155/'],
                'Manasquan Inlet': ['http://www.surfline.com/surf-forecasts/spot/manasquan-inlet_4278/'],
                'Jenkinsons': ['http://www.surfline.com/surf-forecasts/spot/jenkinsons_5183/'],
                'Bay Head': ['http://www.surfline.com/surf-forecasts/spot/bay-head_5182/'],
                'Mantoloking': ['http://www.surfline.com/surf-forecasts/spot/mantoloking_6319/'],
                'Lavallette': ['http://www.surfline.com/surf-forecasts/spot/lavallette_5181/'],
                'Ortley Beach': ['http://www.surfline.com/surf-forecasts/spot/ortley-beach_5180/'],
                'Casino Pier': ['http://www.surfline.com/surf-forecasts/spot/casino-pier_4279/'],
                'Seaside Heights': ['http://www.surfline.com/surf-forecasts/spot/seaside-heights_5179/'],
                'Seaside Park': ['http://www.surfline.com/surf-forecasts/spot/seaside-park_5178/'],
                'Island Beach State': ['http://www.surfline.com/surf-forecasts/spot/island-beach-state-park_5177/'],
                'Hudson Avenue, Harvey Cedars': ['http://www.surfline.com/surf-forecasts/spot/hudson-ave_5176/'],
                'Long Beach Island': ['http://www.surfline.com/surf-forecasts/spot/long-beach-island_4280/'],
                '7-11': ['http://www.surfline.com/surf-forecasts/spot/7-11_5175/'],
                'Holyoke': ['http://www.surfline.com/surf-forecasts/spot/holyoke_5174/'],
                'The WoodenJetty': ['http://www.surfline.com/surf-forecasts/spot/the-woodenjetty_5173/'],
                '10th Street North to 14th Street North': ['http://www.surfline.com/surf-forecasts/spot/10th-street-north-to-14th-street-north_5172/'],
                'Brigantine Jetty': ['http://www.surfline.com/surf-forecasts/spot/brigantine-jetty_5171/'],
                'Seaside Road, Brigantine': ['http://www.surfline.com/surf-forecasts/spot/seaside-road_144653/'],
                'Crystals': ['http://www.surfline.com/surf-forecasts/spot/crystals_5170/'],
                'States Avenue': ['http://www.surfline.com/surf-forecasts/spot/states-avenue_5169/'],
                'South Carolina Avenue': ['http://www.surfline.com/surf-forecasts/spot/south-carolina-avenue_5168/'],
                'Ventnor Pier': ['http://www.surfline.com/surf-forecasts/spot/ventnor-pier_5167/'],
                'Margate Pier': ['http://www.surfline.com/surf-forecasts/spot/margate-pier_5166/'],
                '32nd Street': ['http://www.surfline.com/surf-forecasts/spot/32nd-street_5165/'],
                '1st Street, Ocean City, NJ': ['http://www.surfline.com/surf-forecasts/spot/1st-st_4281/'],
                'North Street to 3rd Street Jetty': ['http://www.surfline.com/surf-forecasts/spot/north-street-to-3rd-street-jetty_5575/'],
                '7th Street': ['http://www.surfline.com/surf-forecasts/spot/7th-street_5576/'],
                'Sumner Avenue': ['http://www.surfline.com/surf-forecasts/spot/sumner-avenue_5577/'],
                '36th Street to 42nd Street': ['http://www.surfline.com/surf-forecasts/spot/36th-street-to-42nd-street_5578/'],
                'Avalon 10-14th Street': ['http://www.surfline.com/surf-forecasts/spot/avalon-10-14th-street_128396/'],
                '26th to 30th Street Pier': ['http://www.surfline.com/surf-forecasts/spot/26th-to-30th-street-pier_5579/'],
                'Nuns Beach': ['http://www.surfline.com/surf-forecasts/spot/nuns-beach_5580/'],
                '2nd Street to 10th Street': ['http://www.surfline.com/surf-forecasts/spot/2nd-ave-to-10th-ave_5581/'],
                'Stegers Beach': ['http://www.surfline.com/surf-forecasts/spot/stegers-beach_5582/'],
                'Trestles, The Rocks': ['http://www.surfline.com/surf-forecasts/spot/trestles-the-rocks_5583/'],
                'Poverty Beach': ['http://www.surfline.com/surf-forecasts/spot/poverty-beach_5584/'],
                'Queen Street': ['http://www.surfline.com/surf-forecasts/spot/queen-street_5585/'],
                'Stockton Avenue': ['http://www.surfline.com/surf-forecasts/spot/stockton-avenue_5586/'],
                'Grant Street': ['http://www.surfline.com/surf-forecasts/spot/grant-street-beach_5587/'],
                'Broadway Beach': ['http://www.surfline.com/surf-forecasts/spot/broadway-beach_5588/'],
                'The Cove': ['http://www.surfline.com/surf-forecasts/spot/the-cove_5589/']
            },
            'Maryland-Delaware': {
                'Naval Jetties': ['http://www.surfline.com/surf-forecasts/spot/naval-jetties_5192/'],
                'Gordons Pond': ['http://www.surfline.com/surf-forecasts/spot/gordons-pond_5191/'],
                'Dewey Beach': ['http://www.surfline.com/surf-forecasts/spot/dewey-beach_5190/'],
                'Indian River Inlet': ['http://www.surfline.com/surf-forecasts/spot/indian-river-inlet_5187/'],
                'Bethany Beach': ['http://www.surfline.com/surf-forecasts/spot/bethany-beach_5189/'],
                'Fenwick Island': ['http://www.surfline.com/surf-forecasts/spot/fenwick-island_5188/'],
                'North End to Ocean City Inlet': ['http://www.surfline.com/surf-forecasts/spot/north-end-to-ocean-city-inlet_5186/'],
                '8th Street, Ocean City, MD': ['http://www.surfline.com/surf-forecasts/spot/8th-st_4406/'],
                'Assateague': ['http://www.surfline.com/surf-forecasts/spot/assateague_5185/'],
            }
        },
        'Virginia - Outer Banks': {
            'Virginia': {
                'Fishermans Island': ['http://www.surfline.com/surf-forecasts/spot/fishermans-island_5212/'],
                'North End 83rd - 86th Street': ['http://www.surfline.com/surf-forecasts/spot/83rd-to-86th-st-north-end_5211/'],
                'North End 72nd Street': ['http://www.surfline.com/surf-forecasts/spot/north-end-72nd-st_145754/'],
                'North End 42nd - 46th Street': ['http://www.surfline.com/surf-forecasts/spot/42nd-to-46th-st-north-end_106919/'],
                '15th Street Pier': ['http://www.surfline.com/surf-forecasts/spot/15th-street-pier_5210/'],
                '1st St. Jetty to Pier': ['http://www.surfline.com/surf-forecasts/spot/1st-st-jetty-to-pier_4407/'],
                '1st Street Jetty Fixed': ['http://www.surfline.com/surf-forecasts/spot/1st-st-jetty_133157/'],
                'Croatan Jetty': ['http://www.surfline.com/surf-forecasts/spot/croatan-jetty_133158/'],
                'Croatan/Pendleton Surf': ['http://www.surfline.com/surf-forecasts/spot/croatan-to-pendleton_5208/'],
                'Camp Pendleton': ['http://www.surfline.com/surf-forecasts/spot/camp-pendleton_5206/'],
                'Sandbridge Beach': ['http://www.surfline.com/surf-forecasts/spot/sandbridge-beach_5207/']
            },
            'Norther Outer Banks': {
                'Corolla': ['http://www.surfline.com/surf-forecasts/spot/corolla_5242/'],
                'Duck Pier': ['http://www.surfline.com/surf-forecasts/spot/duck-pier_5241/'],
                'Kitty Hawk Pier': ['http://www.surfline.com/surf-forecasts/spot/kitty-hawk-pier_5240/'],
                'Eckner Street, Kitty Hawk': ['http://www.surfline.com/surf-forecasts/spot/eckner-street_106914/'],
                'Old Station/Laundromats': ['http://www.surfline.com/surf-forecasts/spot/old-station-laundromats_5239/'],
                'Avalon Pier': ['http://www.surfline.com/surf-forecasts/spot/avalon-pier_5238/'],
                '3rd Street': ['http://www.surfline.com/surf-forecasts/spot/3rd-st_4408/'],
                '1st Street': ['http://www.surfline.com/surf-forecasts/spot/1st-st_5237/'],
                'Bath House': ['http://www.surfline.com/surf-forecasts/spot/bath-house_69923/'],
                'Abalone Street, Nags Head': ['http://www.surfline.com/surf-forecasts/spot/abalone-st_133159/'],
                'Nags Head Pier': ['http://www.surfline.com/surf-forecasts/spot/nags-head-pier_5236/'],
                'Jennettes Pier': ['http://www.surfline.com/surf-forecasts/spot/jennettes-pier-northside_111858/'],
                'Jennettes Pier Fish Cam': ['http://www.surfline.com/surf-forecasts/spot/jennettes-pier-fishing-cam_116831/'],
                'Jennettes Pier SS': ['http://www.surfline.com/surf-forecasts/spot/jennettes-pier-southside_95460/']
            },
            'Hatteras Island': {
                'Pea Island': ['http://www.surfline.com/surf-forecasts/spot/pea-island_5235/'],
                'S Turns': ['http://www.surfline.com/surf-forecasts/spot/s-turns_5234/'],
                'S-Turns, Rodanthe': ['http://www.surfline.com/surf-forecasts/spot/s-turns_4410/'],
                'Waves and Salvo': ['http://www.surfline.com/surf-forecasts/spot/waves-and-salvo_5232/'],
                'Avon Pier': ['http://www.surfline.com/surf-forecasts/spot/avon-pier_5231/'],
                'Cape Hatteras Lighthouse': ['http://www.surfline.com/surf-forecasts/spot/cape-hatteras-lighthouse_5230/'],
                'Billy Mitchell, Frisco': ['http://www.surfline.com/surf-forecasts/spot/billy-mitchell_139184/'],
                'Frisco Pier': ['http://www.surfline.com/surf-forecasts/spot/frisco-pier_5229/'],
                'Ocracoke': ['http://www.surfline.com/surf-forecasts/spot/ocracoke_5228/'],
                'Summerplace Drive': ['http://www.surfline.com/surf-forecasts/spot/summerplace-dr_145175/']
            }
        }
    }



spot = spotLocation_NorthAmerica[pickRegion]

def user_pick():


























