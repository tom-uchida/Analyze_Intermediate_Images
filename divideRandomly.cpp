#include <fstream>
#include <iostream>

#include "divideRandomly.h"


DivideRandomly::DivideRandomly( const kvs::PolygonObject* ply, const size_t repeat_level )
{
    DoRandomDivision( ply, repeat_level );
}

void DivideRandomly::DoRandomDivision( const kvs::PolygonObject* ply, const size_t repeat_level ) {
    size_t num_input_points = ply->numberOfVertices();
    std::cout << "Num. of input points : " << num_input_points << std::endl;
    std::cout << "Repeat level         : " << repeat_level << std::endl;
    std::cout << "P / L                : " << num_input_points / repeat_level << std::endl;
    
    //long* k_random = new R_INT[num_input_points];
    

    // Stochastic acceptance of the current point
    // double dice = (double)rand() / (double)RAND_MAX ; 
    // if ( dice <= reduction_ratio ) {
    //     m_sampling_pt_index.push_back(k_random[k]);
    // }


    //     void ParticleBasedRenderer::Engine::create_buffer_object( const kvs::PointObject* point )
    // {
    //     KVS_ASSERT( point->coords().size() == point->colors().size() );

    //     kvs::ValueArray<kvs::Real32> coords = point->coords();
    //     kvs::ValueArray<kvs::UInt8> colors = point->colors();
    //     kvs::ValueArray<kvs::Real32> normals = point->normals();
    //     if ( m_enable_shuffle )
    //     {
    //         kvs::UInt32 seed = 12345678;
    //         coords = ::ShuffleArray<3>( point->coords(), seed );
    //         colors = ::ShuffleArray<3>( point->colors(), seed );
    //         if ( m_has_normal )
    //         {
    //             normals = ::ShuffleArray<3>( point->normals(), seed );
    //         }
    //     }

    //     if ( !m_vbo ) m_vbo = new kvs::VertexBufferObject [ repetitionLevel() ];

    //     const size_t nvertices = point->numberOfVertices();
    //     const size_t rem = nvertices % repetitionLevel();
    //     const size_t quo = nvertices / repetitionLevel();
    //     for ( size_t i = 0; i < repetitionLevel(); i++ )
    //     {
    //         const size_t count = quo + ( i < rem ? 1 : 0 );
    //         const size_t first = quo * i + kvs::Math::Min( i, rem );
    //         const size_t coord_size = count * sizeof(kvs::Real32) * 3;
    //         const size_t color_size = count * sizeof(kvs::UInt8) * 3;
    //         const size_t normal_size = m_has_normal ? count * sizeof(kvs::Real32) * 3 : 0;
    //         const size_t byte_size = coord_size + color_size + normal_size;
    //         m_vbo[i].create( byte_size );

    //         m_vbo[i].bind();
    //         m_vbo[i].load( coord_size, coords.data() + first * 3, 0 );
    //         m_vbo[i].load( color_size, colors.data() + first * 3, coord_size );
    //         if ( m_has_normal )
    //         {
    //             m_vbo[i].load( normal_size, normals.data() + first * 3, coord_size + color_size );
    //         }
    //         m_vbo[i].unbind();
    //     }
    // }
}