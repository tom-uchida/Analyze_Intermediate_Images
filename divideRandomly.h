#ifndef _DivideRandomly_H__
#define _DivideRandomly_H__

#include <kvs/PolygonObject>

class DivideRandomly {

public:
	DivideRandomly( const kvs::PolygonObject* ply, const size_t repeat_level );

private:
    void DoRandomDivision( const kvs::PolygonObject* ply, const size_t repeat_level );
}; // End class

#endif