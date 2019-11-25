import wikipedia as wikipedia
import csv

def savePages(data):
  # clear the current file to prevent content override
  with open('plantData.csv','w+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Plant Name','Page Data',""])

  for plantName in data:
    pageContent = wikipedia.page(plantName).content
    with open('plantData.csv','a',newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow([plantName,pageContent,""])
      print("saved",plantName)

if __name__ == '__main__':
  
  plantNames = [
    'Linnaea_×_grandiflora','Acer_palmatum','Acer_truncatum','Aesculus_pavia',
    'Agave_parryi','Aloe_vera','Anisacanthus_quadrifidus',
    'Asparagus_Densiflorus','Astrolepis_sinuata',
    'Bignonia_capreolata','buchloe_dactyloides','Buddleja_davidii','Buxus_microphylla',
    'Buxus_sempervirens',
    'Caladium','Callicarpa_americana','Cercis_canadensis','Calyptocarpus_vialis','Pecan',
    'Chrysactinia_mexicana','Coreopsis_lanceolata','Cotinus_coggygria','Chamaemelum_nobile',
    'Chasmanthium_latifolium','Chasmanthium_sessiliflorum','Chilopsis','Chrysactinia_mexicana',
    'Meyer_lemon','Cordyline_australis','Cordyline_fruticosa','Coreopsis_grandiflora',
    'Echinacea_paradoxa','Euphorbia_myrsinites','Hesperaloe_funifera',
    'Hydrangea_quercifolia','juniperus_horizontalis','lantana_urticoides',
    'Liriope_muscari','magnolia_soulangeana','Miscanthus_sinensis',
    'Muhlenbergia_lindheimeri','Nerium','Opuntia_rufida',
    'Phlox_divaricata','Phoenix_reclinata','Pyrus_calleryana',
    'Rhododendron_japonicum','Rubus_idaeus','Salvia_guaranitica',
    'Salvia_pachyphylla',
    ]
  print(len(plantNames),"to be saved")
  savePages(plantNames)