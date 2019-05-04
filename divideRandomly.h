#ifndef _DivideRandomly_H__
#define _DivideRandomly_H__

#include <kvs/PolygonObject>
#include <kvs/PointObject>

class DivideRandomly {

public:
	DivideRandomly( const kvs::PolygonObject* _ply, const size_t _repeat_level );

    void shuffle();
    void writeToSPBRFile( std::string _out_file_path );

private:
    const kvs::PolygonObject* m_ply;
    kvs::PointObject* m_point;
    size_t m_num_of_input_points;
    int m_num_of_points_in_each_ensemble;
    const float m_repeat_level;
}; // End class

#endif