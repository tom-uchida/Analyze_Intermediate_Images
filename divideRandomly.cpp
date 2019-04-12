#include <fstream>
#include <iostream>

#include "divideRandomly.h"
#include "shuffle.h"
#include "writeSPBR.h"

// #include <cmath>
// #include <vector>
// #include <math.h>


DivideRandomly::DivideRandomly( const kvs::PolygonObject* ply, const size_t repeat_level )
{
    DoRandomDivision( ply, repeat_level );
}

void DivideRandomly::DoRandomDivision( const kvs::PolygonObject* ply, const size_t repeat_level ) {
    size_t num_of_input_points = ply->numberOfVertices();
    int num_of_points_in_each_ensamble = (int)num_of_input_points / (int)repeat_level;
    std::cout << "Num. of input points : " << num_of_input_points << std::endl;
    std::cout << "Repeat level         : " << repeat_level << std::endl;
    std::cout << "Num. of points in each ensamble : " << num_of_points_in_each_ensamble << std::endl;

    // Shuffle
    kvs::PointObject* object = new kvs::PointObject( *ply );
    Shuffle shuffle_engine( object );
    object->setSize( 1 );
    object->updateMinMaxCoords();

    bool hasNormal = false;
    bool hasColor  = false;
    if ( num_of_input_points == object->numberOfNormals() ) hasNormal   = true; 
    if ( num_of_input_points == object->numberOfColors() )  hasColor    = true;
    kvs::ValueArray<kvs::Real32> coords        = object->coords();

    // Divide
    for ( size_t j = 0; j < repeat_level; j++ ) {
        for ( size_t i = 0; i < num_of_points_in_each_ensamble; i++ ) {
        }
    }

    // Write to spbr file
    for ( size_t j = 0; j < repeat_level; j++ ) {
        for ( size_t i = 0; i < num_of_points_in_each_ensamble; i++ ) {
            std::string out_spbr_file_name = "OUTPUT_DATA/Ensamble";
            std::ostringstream oss;
            oss << j+1;
            out_spbr_file_name += oss.str();
            out_spbr_file_name += ".spbr";
            
            writeSPBR(  /* kvs::PointObject* */ object,
                        /* std::string       */ out_spbr_file_name,
                        /* WritingDataType   */ Ascii );

        } // end for
    } // end for
} // End DoRandomDivision()