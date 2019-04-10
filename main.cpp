// =====================================
//      Analyze Intermediate Images
// =====================================

#include <iostream>
#include <cstring> 
#include <cstdlib>
#include <vector>
#include "importPointClouds.h"
#include "writeSPBR.h"
#include "divideRandomly.h"

#include <kvs/PolygonObject>
#include <kvs/PointObject>
#include <kvs/glut/Application> 
#include <kvs/glut/Screen>
#include <kvs/Camera>
#include <kvs/PointRenderer> 
#include <kvs/Coordinate> 

const char OUT_FILE[] = "SPBR_DATA/output.spbr";

int main( int argc, char** argv ) {
    char outSPBRfile[512];
    strcpy( outSPBRfile, OUT_FILE );

    if ( argc != 2 ) {
        std::cout   << "\nUSAGE   : "    << argv[0] << " [input_file]\n"
                    << "Example : "      << argv[0] << " input.ply\n" << std::endl;
        exit(1);

    } else if ( argc >= 3) {
        strcpy( outSPBRfile, argv[2] );
    }
    
    // =========================
    //  STEP 1: Read input data
    // =========================
    ImportPointClouds *ply = new ImportPointClouds( argv[1] );
    ply->updateMinMaxCoords();
    std::cout << "PLY Min, Max Coords:" << std::endl;
    std::cout << "Min : " << ply->minObjectCoord() << std::endl;
    std::cout << "Max : " << ply->maxObjectCoord() << std::endl;

    // ==========================
    //  STEP 2: Set repeat level
    // ==========================
    size_t repeat_level = 1;
    std::cout   << "\nInput repeat level (the default repeat level is " << repeat_level;
    std::cout   << ") : "; 
    std::cin    >> repeat_level;

    // =========================================================
    //  STEP 3: Randomly, divide input data by the repeat level
    // =========================================================
    DivideRandomly *dr = new DivideRandomly( ply, repeat_level );

    // ----- Write .spbr file -----
    // WritingDataType type = Ascii;
    // writeSPBR(  ply,                    /* kvs::PolygonObject *_ply        */  
    //             outSPBRfile,            /* char*              _filename    */  
    //             atof(argv[3]),          /* float              _correct_parameter */
    //             type                    /* WritingDataType    _type        */
    //         );    

    
    kvs::PointObject* object = new kvs::PointObject( *ply );
    object->setSize( 1 );
    object->updateMinMaxCoords(); 



    // ----- Exec. SPBR -----
    // std::string out_noised_spbr( outSPBRfile );
    // std::string EXEC("spbr ");
    // EXEC += out_noised_spbr;
    // system( EXEC.c_str() );

    return 0;
} // End main()