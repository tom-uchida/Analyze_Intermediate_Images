// =====================================
//      Analyze Intermediate Images
// =====================================

#include <iostream>
#include <cstring> 
#include <cstdlib>
#include <vector>
#include "importPointClouds.h"
#include "divideRandomly.h"

#include <kvs/PolygonObject>
#include <kvs/PointObject>
#include <kvs/glut/Application> 
#include <kvs/glut/Screen>
#include <kvs/Camera>
#include <kvs/PointRenderer> 
#include <kvs/Coordinate> 

const char OUT_FILE_PATH[] = "OUTPUT_DATA/LR10/";

int main( int argc, char** argv ) {
    char out_file_path[512];
    strcpy( out_file_path, OUT_FILE_PATH );

    if ( argc != 3 ) {
        std::cout   << "\nUSAGE   : "    << argv[0] << " [input_file] [output_path]\n"
                    << "Example : "      << argv[0] << " input.ply OUTPUT_DATA/LR10/\n" << std::endl;
        exit(1);

    } else if ( argc == 3) {
        strcpy( out_file_path, argv[2] );
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

    // ===============================================================
    //  STEP 3: Randomly, divide input point data by the repeat level
    // ===============================================================
    DivideRandomly *dr = new DivideRandomly( ply, repeat_level );
    dr->shuffle();
    dr->writeToSPBRFile( out_file_path );

    return 0;
} // End main()