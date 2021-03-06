import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HGCalRecProducers.HGCalUncalibRecHit_cfi import *
from RecoLocalCalo.HGCalRecProducers.HGCalRecHit_cfi import *

# patch particle flow clusters for HGC into local reco sequence
# (for now until global reco is going with some sort of clustering)
from RecoParticleFlow.PFClusterProducer.particleFlowRecHitHGC_cff import *
from RecoParticleFlow.PFClusterProducer.particleFlowClusterHGC_cfi import *
from RecoLocalCalo.HGCalRecProducers.hgcalLayerClusters_cff import hgcalLayerClusters
from RecoLocalCalo.HGCalRecProducers.hgcalMultiClusters_cfi import hgcalMultiClusters

from RecoHGCal.TICL.ticlSeedingRegionProducer_cfi import ticlSeedingRegionProducer
from RecoHGCal.TICL.ticlLayerTileProducer_cfi import ticlLayerTileProducer
from RecoHGCal.TICL.trackstersProducer_cfi import trackstersProducer
from RecoHGCal.TICL.filteredLayerClustersProducer_cfi import filteredLayerClustersProducer
from RecoHGCal.TICL.multiClustersFromTrackstersProducer_cfi import multiClustersFromTrackstersProducer

## withReco: requires full reco of the event to run this part
## i.e. collections of generalTracks can be accessed
def TICL_iterations_withReco(process):
  process.FEVTDEBUGHLTEventContent.outputCommands.extend(['keep *_multiClustersFromTracksters*_*_*'])

  process.ticlLayerTileProducer = ticlLayerTileProducer.clone()

  process.ticlSeedingTrk = ticlSeedingRegionProducer.clone(
    algoId = 1
  )

  process.filteredLayerClustersTrk = filteredLayerClustersProducer.clone(
    clusterFilter = "ClusterFilterByAlgo",
    algo_number = 8,
    iteration_label = "Trk"
  )

  process.trackstersTrk = trackstersProducer.clone(
    filtered_mask = cms.InputTag("filteredLayerClustersTrk", "Trk"),
    seeding_regions = "ticlSeedingTrk",
    missing_layers = 3,
    min_clusters_per_ntuplet = 5,
    min_cos_theta = 0.99, # ~10 degrees                                              
    min_cos_pointing = 0.9
  )

  process.multiClustersFromTrackstersTrk = multiClustersFromTrackstersProducer.clone(
      label = "TrkMultiClustersFromTracksterByCA",
      Tracksters = "trackstersTrk"
  )


  process.ticlSeedingGlobal = ticlSeedingRegionProducer.clone(
    algoId = 2
  )

  process.filteredLayerClustersMIP = filteredLayerClustersProducer.clone(
      clusterFilter = "ClusterFilterBySize",
      algo_number = 8,
      max_cluster_size = 2, # inclusive
      iteration_label = "MIP"
  )

  process.trackstersMIP = trackstersProducer.clone(
      filtered_mask = cms.InputTag("filteredLayerClustersMIP", "MIP"),
      seeding_regions = "ticlSeedingGlobal",
      missing_layers = 3,
      min_clusters_per_ntuplet = 15,
      min_cos_theta = 0.99, # ~10 degrees
      min_cos_pointing = 0.9
  )

  process.multiClustersFromTrackstersMIP = multiClustersFromTrackstersProducer.clone(
      label = "MIPMultiClustersFromTracksterByCA",
      Tracksters = "trackstersMIP"
  )

  process.filteredLayerClusters = filteredLayerClustersProducer.clone(
      clusterFilter = "ClusterFilterByAlgoAndSize",
      min_cluster_size = 2,
      algo_number = 8,
      iteration_label = "algo8",
      LayerClustersInputMask = "trackstersMIP"
  )

  process.tracksters = trackstersProducer.clone(
      original_mask = "trackstersMIP",
      filtered_mask = cms.InputTag("filteredLayerClusters", "algo8"),
      seeding_regions = "ticlSeedingGlobal",
      missing_layers = 2,
      min_clusters_per_ntuplet = 15,
      min_cos_theta = 0.94, # ~20 degrees
      min_cos_pointing = 0.7
  )

  process.multiClustersFromTracksters = multiClustersFromTrackstersProducer.clone(
      Tracksters = "tracksters"
  )

  process.hgcalMultiClusters = hgcalMultiClusters
  process.TICL_Task = cms.Task(
      process.ticlLayerTileProducer,
      process.ticlSeedingTrk,
      process.filteredLayerClustersTrk,
      process.trackstersTrk,
      process.multiClustersFromTrackstersTrk,
      process.ticlSeedingGlobal,
      process.filteredLayerClustersMIP,
      process.trackstersMIP,
      process.multiClustersFromTrackstersMIP,
      process.filteredLayerClusters,
      process.tracksters,
      process.multiClustersFromTracksters)
  process.schedule.associate(process.TICL_Task)
  return process


## TICL_iterations: to be run with local HGCAL reco only
## i.e. collections of generalTracks (track-seeded iteration) NOT available
def TICL_iterations(process):
  process.FEVTDEBUGHLTEventContent.outputCommands.extend(['keep *_multiClustersFromTracksters*_*_*'])

  process.ticlLayerTileProducer = ticlLayerTileProducer.clone()

  process.ticlSeedingGlobal = ticlSeedingRegionProducer.clone(
    algoId = 2
  )

  process.filteredLayerClustersMIP = filteredLayerClustersProducer.clone(
      clusterFilter = "ClusterFilterBySize",
      algo_number = 8,
      max_cluster_size = 2, # inclusive
      iteration_label = "MIP"
  )

  process.trackstersMIP = trackstersProducer.clone(
      filtered_mask = cms.InputTag("filteredLayerClustersMIP", "MIP"),
      seeding_regions = "ticlSeedingGlobal",
      missing_layers = 3,
      min_clusters_per_ntuplet = 15,
      min_cos_theta = 0.99 # ~10 degrees
  )

  process.multiClustersFromTrackstersMIP = multiClustersFromTrackstersProducer.clone(
      label = "MIPMultiClustersFromTracksterByCA",
      Tracksters = "trackstersMIP"
  )

  process.filteredLayerClusters = filteredLayerClustersProducer.clone(
      clusterFilter = "ClusterFilterByAlgoAndSize",
      min_cluster_size = 2,
      algo_number = 8,
      iteration_label = "algo8"
  )

  process.tracksters = trackstersProducer.clone(
      original_mask = "trackstersMIP",
      filtered_mask = cms.InputTag("filteredLayerClusters", "algo8"),
      seeding_regions = "ticlSeedingGlobal",
      missing_layers = 2,
      min_clusters_per_ntuplet = 15,
      min_cos_theta = 0.94, # ~20 degrees
      min_cos_pointing = 0.7
  )

  process.multiClustersFromTracksters = multiClustersFromTrackstersProducer.clone(
      Tracksters = "tracksters"
  )

  process.HGCalUncalibRecHit = HGCalUncalibRecHit
  process.HGCalRecHit = HGCalRecHit
  process.hgcalLayerClusters = hgcalLayerClusters
  process.hgcalMultiClusters = hgcalMultiClusters
  process.TICL_Task = cms.Task(process.HGCalUncalibRecHit,
      process.HGCalRecHit,
      process.hgcalLayerClusters,
      process.filteredLayerClustersMIP,
      process.ticlLayerTileProducer,
      process.ticlSeedingGlobal,
      process.trackstersMIP,
      process.multiClustersFromTrackstersMIP,
      process.filteredLayerClusters,
      process.tracksters,
      process.multiClustersFromTracksters,
      process.hgcalMultiClusters)
  process.schedule = cms.Schedule(process.raw2digi_step,process.FEVTDEBUGHLToutput_step)
  process.schedule.associate(process.TICL_Task)
  return process

