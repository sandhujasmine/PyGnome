'''
Created on Mar 4, 2013
'''
from datetime import timedelta

from colander import (
    SchemaNode,
    MappingSchema,
    Bool,
    Float,
    Range,
    TupleSchema,
    Int,
    String,
    SequenceSchema,
    drop,
    deferred
    )

import gnome
from gnome.persist import validators, extend_colander, base_schema


class SpillContainerPair(MappingSchema):
    certain_spills = base_schema.OrderedCollection()
    uncertain_spills = base_schema.OrderedCollection(missing=drop)  # only present if uncertainty is on

class MapItem(TupleSchema):
    type = SchemaNode( String() )
    id   = SchemaNode( String() )
    
class MapList(MappingSchema):
    map = MapItem()
    output_map = MapItem(missing=drop)    

class Map(base_schema.Id, MappingSchema):
    map_bounds = MapBounds()
    filename = SchemaNode(String(), missing=drop)
    refloat_halflife = SchemaNode( Float(), missing=drop)

class Model(base_schema.Id, MappingSchema):
    time_step = SchemaNode( Float()) 
    start_time= SchemaNode(extend_colander.LocalDateTime(), validator=validators.convertable_to_seconds)
    duration = SchemaNode(extend_colander.TimeDelta() )   # put a constraint for max duration?
    movers = base_schema.OrderedCollection()
    environment = base_schema.OrderedCollection()
    uncertain = SchemaNode( Bool() )
    spills = SpillContainerPair()
    maps = MapList()