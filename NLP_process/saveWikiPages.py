import wikipedia as wikipedia
import csv

def savePages(srNo,pageName,wikiLink):
  pageContent = wikipedia.page(pageName).content
  with open('plantData.csv','a',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([srNo,pageName,wikiLink,pageContent,""])
    print("saved",pageName)

def loadPlantNames():
  pageCounter = 0
  # Clear the plant data File to prevent data override 
  with open('plantData.csv','w+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['SR No','Plant Name','Wiki link','Page Data',""])

  with open('plantList.csv') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      pageCounter += 1
      pageName = row[1]
      wikiLink = row[2]
      if(pageName == 'NILL'):
        pass
      else:
        savePages(pageCounter,pageName,wikiLink)


if __name__ == '__main__':
  # plantNames = [
  #   'Linnaea_×_grandiflora','Acer_palmatum','Acer_truncatum','Aesculus_pavia',
  #   'Agave_parryi','Aloe_vera','Anisacanthus_quadrifidus',
  #   'Asparagus_Densiflorus','Astrolepis_sinuata',
  #   'Bignonia_capreolata','buchloe_dactyloides','Buddleja_davidii','Buxus_microphylla',
  #   'Buxus_sempervirens',
  #   'Caladium','Callicarpa_americana','Cercis_canadensis','Calyptocarpus_vialis','Pecan',
  #   'Chrysactinia_mexicana','Coreopsis_lanceolata','Cotinus_coggygria','Chamaemelum_nobile',
  #   'Chasmanthium_latifolium','Chasmanthium_sessiliflorum','Chilopsis','Chrysactinia_mexicana',
  #   'Meyer_lemon','Cordyline_australis','Cordyline_fruticosa','Coreopsis_grandiflora',
  #   'Echinacea_paradoxa','Euphorbia_myrsinites','Hesperaloe_funifera',
  #   'Hydrangea_quercifolia','juniperus_horizontalis','lantana_urticoides',
  #   'Liriope_muscari','magnolia_soulangeana','Miscanthus_sinensis',
  #   'Muhlenbergia_lindheimeri','Nerium','Opuntia_rufida',
  #   'Phlox_divaricata','Phoenix_reclinata','Pyrus_calleryana',
  #   'Rhododendron_japonicum','Rubus_idaeus','Salvia_guaranitica',
  #   'Salvia_pachyphylla',
  #   ]
  loadPlantNames()
