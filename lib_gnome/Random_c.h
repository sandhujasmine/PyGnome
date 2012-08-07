/*
 *  Random_c.h
 *  gnome
 *
 *  Created by Generic Programmer on 10/18/11.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 */

#ifndef __Random_c__
#define __Random_c__

#include "Basics.h"
#include "TypeDefs.h"
#include "Mover_c.h"

#ifdef pyGNOME
#define TMap Map_c
#endif

class TMap;

class Random_c : virtual public Mover_c {
	
public:
	double fDiffusionCoefficient; //cm**2/s
	TR_OPTIMZE fOptimize; // this does not need to be saved to the save file
	double fUncertaintyFactor;		// multiplicative factor applied when uncertainty is on
	Boolean bUseDepthDependent;
	
	Random_c (TMap *owner, char *name);
	Random_c() {}
	virtual OSErr 		PrepareForModelRun(); 
	virtual OSErr 		PrepareForModelStep(const Seconds&, const Seconds&, bool); // AH 07/10/2012
	virtual void 		ModelStepIsDone();
	virtual WorldPoint3D       GetMove(const Seconds& model_time, Seconds timeStep,long setIndex,long leIndex,LERec *theLE,LETYPE leType);
	
	
};

#undef TMap
#endif
