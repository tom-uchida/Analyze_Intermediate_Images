#include <fstream>
#include <iostream>
#include <kvs/PointObject>

#include "divideRandomly.h"

// default
const float NORMAL[3]   = { 0.0, 0.0, 0.0 };
const int   COLOR[3]    = { 255, 255, 255 };

DivideRandomly::DivideRandomly( const kvs::PolygonObject* _ply, const size_t _repeat_level ) :
    m_ply( _ply ),
    m_repeat_level( _repeat_level )
{
    m_num_of_input_points = m_ply->numberOfVertices();
    m_num_of_points_in_each_ensemble = (int)m_num_of_input_points / (int)m_repeat_level;
    std::cout << "Num. of input points : " << m_num_of_input_points << std::endl;
    std::cout << "Repeat level         : " << m_repeat_level << std::endl;
    std::cout << "Num. of points in each ensemble : " << m_num_of_points_in_each_ensemble << std::endl;
}

// Shuffle
void DivideRandomly::shuffle() {
    // kvs::PointObject* point = new kvs::PointObject( *m_ply );
    m_point = new kvs::PointObject( *m_ply );
    // std::cout << "Before    : " << m_point->coord( 0 ) << std::endl;

    // Get the number of points in the PointObject.
    const size_t npoints = m_point->numberOfVertices();

    // Create shuffled indices for temporary arrays
    kvs::ValueArray<int> index( npoints ); // We need npoints indices.
    for ( size_t i = 0; i < npoints; i++ ) index[i] = static_cast<int>( i );
    std::random_shuffle( index.begin(), index.end() );

    // Create the shuffled "coords" array.
    {
        // Temporary array for coords (initialized to empty)
        //   x0 y0 z0 x1 y1 z1 x2 y2 z2 ... 
        kvs::ValueArray<kvs::Real32> shuffled_coords( npoints * 3 ); 

        // Define a pointer to an element of the array. 
        //   It is initialized to &(coords[0]).
        kvs::Real32* pcoords = shuffled_coords.pointer(); 

        // Set coords of the index[i]-th point 
        //   as the i-th elemeht of the array.
        for ( size_t i = 0; i < npoints; i++ ) {
            // Set coords of the index[i]-th point 
            //   as the i-th elemeht of the array

            // Get one point(Vector3f) using shuffled index
            const kvs::Vector3f v = m_point->coord( index[i] );

            // Replace
            *(pcoords++) = v.x();
            *(pcoords++) = v.y();
            *(pcoords++) = v.z();
        }

        // Replace coords of the point object with suffled result
        m_point->setCoords( shuffled_coords );
        // std::cout << "test : " << this->coord(0) << std::endl;
    }

    // std::cout << "After     : " << m_point->coord( 0 ) << std::endl;

    // Create the shuffled color array.
    if ( m_point->numberOfColors() == 1 ) m_point->setColor( m_point->color() );
    else if ( m_point->numberOfColors() > 1 )
    {
        // Temporary array for colors (initialized to empty)
        //   r0 g0 b0 r1 g1 b1 r2 g2 b2 ... 
        kvs::ValueArray<kvs::UInt8> colors( npoints * 3 );

        // Define a pointer to an element of the array. 
        //   It is initialized to &(colors[0]).
        kvs::UInt8* pcolors = colors.pointer(); 

        // Set colors of the index[i]-th point 
        //   as the i-th elemeht of the array
        for ( size_t i = 0; i < npoints; i++ )
        {
            const kvs::RGBColor c = m_point->color( index[i] );
            *(pcolors++) = c.r();
            *(pcolors++) = c.g();
            *(pcolors++) = c.b();
        }

        // Replace colors of the point object with suffled result
        m_point->setColors( colors );
    }


    // Create the shuffled surface normal array.
    if ( m_point->numberOfNormals() > 1 )
    {
        // Temporary array for normals (initialized to empty)
        //   nx0 ny0 nz0 nx1 ny1 nz1 nx2 ny2 nz2 ... 
        kvs::ValueArray<kvs::Real32> normals( npoints * 3 );

        // Define a pointer to an element of the array. 
        //   It is initialized to &(normals[0]).
        kvs::Real32* pnormals = normals.pointer(); 

        // Set normals of the index[i]-th point 
        //   as the i-th elemeht of the array
        for ( size_t i = 0; i < npoints; i++ )
        {
            const kvs::Vector3f n = m_point->normal( index[i] );
            *(pnormals++) = n.x();
            *(pnormals++) = n.y();
            *(pnormals++) = n.z();
        }

        // Replace normals of the point object with suffled result
        m_point->setNormals( normals );
    }

    m_point->setSize( 1 );

    // Copy the original bounding-box information to the shuffled point set
    m_point->setMinMaxObjectCoords   (    m_point->minObjectCoord(), 
                                        m_point->maxObjectCoord()   );
    m_point->setMinMaxExternalCoords (    m_point->minExternalCoord(), 
                                        m_point->maxExternalCoord() );
} // End shuffle()

// Write to spbr file
void DivideRandomly::write2SPBRFile( std::string _out_file_path ) {
    // const kvs::PointObject* object = new kvs::PointObject( *m_ply );
    bool hasNormal = false;
    bool hasColor  = false;
    if ( m_num_of_input_points == m_point->numberOfNormals() ) hasNormal   = true; 
    if ( m_num_of_input_points == m_point->numberOfColors() )  hasColor    = true;
    const kvs::ValueArray<kvs::Real32> coords     = m_point->coords();
    const kvs::ValueArray<kvs::Real32> normals    = m_point->normals();
    const kvs::ValueArray<kvs::UInt8>  colors     = m_point->colors();

    for ( size_t j = 0; j < m_repeat_level; j++ ) {
        // Set output file name
        std::string out_spbr_file_name = _out_file_path + "/";
        std::ostringstream oss;
        oss << "ensemble";
        oss << j+1;
        out_spbr_file_name += oss.str();
        out_spbr_file_name += ".spbr";
        std::ofstream fout( out_spbr_file_name.c_str() );
            
        // Set spbr parameter
        fout << "#/SPBR_ASCII_Data"       << std::endl;
        fout << "#/RepeatLevel 1"         << std::endl;
        fout << "#/BGColorRGBByte 0 0 0"  << std::endl;
        fout << "#/ImageResolution 1000"  << std::endl;
        // fout << "#/BoundingBox 0.15 0.15 0 0.85 0.85 0" << std::endl;
        fout << "#/Shading 0"             << std::endl;
        fout << "#/EndHeader"             << std::endl;

        for ( size_t i = 0; i < m_num_of_points_in_each_ensemble; i++ ) {
            // coords
            float x = coords[ 3*j*m_num_of_points_in_each_ensemble + 3*i   ];
            float y = coords[ 3*j*m_num_of_points_in_each_ensemble + 3*i+1 ];
            float z = coords[ 3*j*m_num_of_points_in_each_ensemble + 3*i+2 ];

            // normal(default)
            float nx = NORMAL[0];
            float ny = NORMAL[1];
            float nz = NORMAL[2];
            if ( hasNormal ) {
                nx = normals[ 3*j*m_num_of_points_in_each_ensemble + 3*i   ];
                ny = normals[ 3*j*m_num_of_points_in_each_ensemble + 3*i+1 ];
                nz = normals[ 3*j*m_num_of_points_in_each_ensemble + 3*i+2 ];
            }

            // color(default)
            int r = COLOR[0];
            int g = COLOR[1];
            int b = COLOR[2];
            if ( hasColor ) {
                r = colors[ 3*j*m_num_of_points_in_each_ensemble + 3*i   ];
                g = colors[ 3*j*m_num_of_points_in_each_ensemble + 3*i+1 ];
                b = colors[ 3*j*m_num_of_points_in_each_ensemble + 3*i+2 ];
            }

            // Write to output .spbr file
            fout    << x   << " " << y  << " " << z  << " "
                    << nx  << " " << ny << " " << nz << " "
                    << r   << " " << g  << " " << b  << " " 
                    << std::endl;
        } // end for

        fout.close();

        // Show progress
        std::cout << " ensemble" << j+1 << ".spbr done." << std::endl;
    } // end for

    std::cout << "\nFile export of all ensembles is complete." << std::endl;
} // End writeToSPBRFile()