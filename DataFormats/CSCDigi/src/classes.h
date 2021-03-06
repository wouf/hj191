#include "DataFormats/CSCDigi/interface/CSCWireDigi.h"
#include "DataFormats/CSCDigi/interface/CSCWireDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCRPCDigi.h"
#include "DataFormats/CSCDigi/interface/CSCRPCDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCStripDigi.h"
#include "DataFormats/CSCDigi/interface/CSCStripDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCComparatorDigi.h"
#include "DataFormats/CSCDigi/interface/CSCComparatorDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTDigi.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCALCTDigi.h"
#include "DataFormats/CSCDigi/interface/CSCALCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCorrelatedLCTDigi.h"
#include "DataFormats/CSCDigi/interface/CSCCorrelatedLCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCFEBStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCCFEBStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCDMBStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCDMBStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCTMBStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCTMBStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCDCCFormatStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCDCCFormatStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCALCTStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCALCTStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCDDUStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCDDUStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCDCCStatusDigi.h"
#include "DataFormats/CSCDigi/interface/CSCDCCStatusDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTPreTriggerCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTPreTriggerDigi.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTPreTriggerDigiCollection.h"

// dummy structs to ensure backward compatibility
struct GEMCSCLCTDigi {};
struct GEMCSCLCTDigiCollection {};

#include "DataFormats/Common/interface/Wrapper.h"
#include <vector>
#include <map>
