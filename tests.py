"""
This file contains tests to verify the correctness of the functions you implement in
practicum.py.  This file needs to be in the same directory as your practicum.py file
for it to work.

You can run this file to test your code.  Some tests in the unit test may fail even
if your code is fully correct.  This is because some of the functions you need to
implement have non-deterministic behavior.
"""
import unittest
import practicum

class PracticumTests( unittest.TestCase ):
    """
    Unit tests for the functions that need to be implemented in practicum.py
    """

    def test_reduce(self):
        input = [ 2, 2, None, None ]
        self.assertEqual( input, practicum.reduce( input ) )
        input = [ 2, 4, None, None ]
        self.assertEqual( input, practicum.reduce( input ) )

        self.assertEqual( [ 2, None ], practicum.reduce( [ None, 2 ] ) )
        self.assertEqual( [ 2, 2, None ], practicum.reduce( [ 2, None, 2 ] ) )
        self.assertEqual( [ 2, 4, None ], practicum.reduce( [ 2, None, 4 ] ) )
        self.assertEqual( [ 2, 4, None ], practicum.reduce( [ None, 2, 4 ] ) )

    def test_transpose(self):
        input = [ [ 2, 2 ], [ None, None ] ]
        self.assertEqual( [ [ 2, None ], [ 2, None ] ], practicum.transpose( input ) )
        input = [ [ 2, None ], [ None, 2 ] ]
        self.assertEqual( input, practicum.transpose( input ) )
        self.assertEqual( [ [ 2 ] ], practicum.transpose( [[2]] ) )

    def test_mirror(self):
        input = [ [ 1, 2, 3 ], [ 1, 2, 3 ], [ 1, 2, 3 ] ]
        output = [ [ 3, 2, 1 ], [ 3, 2, 1 ], [ 3, 2, 1 ] ]
        self.assertEqual( output, practicum.mirror( input ) )
        input = [ [ 1, 2 ], [ 3, 4 ] ]
        output = [ [ 2, 1 ], [ 4, 3 ] ]
        self.assertEqual( output, practicum.mirror( input ) )
        input = [ [ 1, None ], [ None, 1 ] ]
        output = [ [ None, 1 ], [ 1, None ] ]
        self.assertEqual( output, practicum.mirror( input ) )

    def test_match_row(self):
        self.assertEqual([ 4, None, None ], practicum.match([2, 2, None]) [0])
        self.assertEqual([ 4, None, 2 ], practicum.match([2, 2, 2, ]) [0])
        self.assertEqual([ 4, None, 4, None ], practicum.match([2, 2, 2, 2])[0])
        self.assertEqual([ 4, None, None ], practicum.match([2, None, 2])[0])
        self.assertEqual([ 2, 8, None, None ], practicum.match([2, 4, None, 4])[0])
        self.assertEqual([ 4, None, 4 ], practicum.match([2, 2, 4])[0])
        self.assertEqual([ 4, 4, None ], practicum.match([4, 2, 2])[0])
        self.assertEqual([ 4, None, 8, None ], practicum.match([2, 2, 4, 4])[0])
        self.assertEqual([ 4, None, None, 4, None ], practicum.match( [ 2, 2, None, 2, 2 ] )[0] )
        self.assertEqual( [4, 2, 4, None ], practicum.match( [ 4, 2, 4, None ] )[0] )
        self.assertEqual( [2, 4, 2, 4 ], practicum.match( [ 2, 4, 2, 4 ] )[0] )

    def test_match_score(self):
        self.assertEqual( 0, practicum.match( [ None, None ] )[1] )
        self.assertEqual( 0, practicum.match( [ 2, None ] )[1] )
        self.assertEqual( 0, practicum.match( [ 2, 4 ] )[1] )
        self.assertEqual( 4, practicum.match( [ 2, 2 ] )[1] )
        self.assertEqual( 4, practicum.match( [ 2, 2, 2 ] )[1] )
        self.assertEqual( 8, practicum.match( [ 2, 2, 2, 2 ] )[1] )
        self.assertEqual( 8, practicum.match( [ 2, 2, None, 2, 2 ] )[1] )
        self.assertEqual( 12, practicum.match( [ 2, 2, None, 4, 4 ] )[1] )

    def test_has_empty_slots(self):
        self.assertFalse( practicum.has_empty_slot( [ [ 1 ] ] ) )
        self.assertTrue( practicum.has_empty_slot( [ [ None ] ] ) )
        self.assertFalse( practicum.has_empty_slot( [ [ 2, 2 ], [ 4, 4 ] ] ) )
        self.assertTrue( practicum.has_empty_slot( [ [ 2, None ], [ 4, 4 ] ] ) )
        self.assertTrue( practicum.has_empty_slot( [ [ 2, None ], [ 4, None ] ] ) )

    def test_has_matches(self):
        self.assertFalse( practicum.has_matches( [ [ 2, None ], [ None, 2 ] ] ) )
        self.assertTrue( practicum.has_matches( [ [ 2, 2 ], [ None, None ] ] ) )
        self.assertTrue( practicum.has_matches( [ [ 2, None ], [ 2, None ] ] ) )
        self.assertFalse( practicum.has_matches( [ [ 2, 4 ], [ 4, 2 ] ] ) )
        self.assertTrue( practicum.has_matches( [ [ 2, None, 2 ], [ None, None, None ], [ None, None, None ] ] ) )
        self.assertFalse( practicum.has_matches( [ [ 2, 4, 2 ], [ None, None, None ], [ None, None, None ] ] ) )
        self.assertTrue( practicum.has_matches( [ [ 2, None, None ], [ None, None, None ], [ 2, None, None ] ] ) )
        self.assertTrue( practicum.has_matches( [ [ None, None, 2 ], [ None, None, 2 ], [ None, None, None ] ] ) )
        self.assertFalse( practicum.has_matches( [ [ 2, None, None ], [ None, None, None ], [ None, None, 2 ] ] ) )
        self.assertFalse( practicum.has_matches( [ [ 2, None, None ], [ None, 2, None ], [ None, None, 2 ] ] ) )

    def test_insert_new_full(self):
        input = [ [ 4, 4 ], [ 4, 4 ] ]
        self.assertEqual( input, practicum.insert_new( input, 4, 1 ) )

    def test_insert_new_empty(self):
        for i in range( 1, 5 ):
            result = practicum.insert_new( [ [ None, None ], [ None, None ] ], i, 1 )
            self.assertEqual( i, self._calculate_not_nones( result ) )
            self.assertEqual( { 2 }, self._extract_elements( result ) )

    def test_insert_difficulty(self):
        """
        This is one of the tests that could fail even if your code is completely correct.  Here we check
         whether your code introduces all three kinds of new elements (2, 4 and 8).  It could happen that
         even when we execute this 9999 times, your code will always insert an 8.  It shouldn't be likely though.
        """
        for i in range( 0, 9999 ):
            result = practicum.insert_new( [ [ None, None, None ],[ None, None, None ],[ None, None, None ] ], 9, 3 )
            found = self._extract_elements( result ) == { 2, 4, 8 }
            if found:
                break
        self.assertTrue( found, msg = "All values are inserted.  Failure does not imply incorrect code." )

    def test_initialize_dimensions_and_nones(self):
        for i in range( 2, 8 ):
            output = practicum.initialize( i, 0, 0 )
            self.assertEqual( i, len( output ) )
            for row in output:
                self.assertEqual( [ None ] * i, row )

    def test_initialize_num_elements(self):
        for i in range( 2, 8 ):
            output = practicum.initialize( 4, i, 1 )
            self.assertEqual( { 2 }, self._extract_elements( output ) )
            self.assertEqual( i, self._calculate_not_nones( output ) )

    def test_initialize_difficulty(self):
        """
        This is one of the tests that could fail even if your code is completely correct.
        """
        for i in range( 1, 4 ):
            values = set()
            found = False
            for j in range( 0, i ):
                values.add( 2 ** ( j + 1 ) )
            for k in range( 0, 9999 ):
                output = practicum.initialize( 10, 10, i )
                if values == self._extract_elements( output ):
                    found = True
                    break
            self.assertTrue( found )

    def test_handle_keypress_directions( self ):
        input = [ [ 2, 2 ], [ None, 4 ] ]
        output, score = practicum.handle_key_press( input, 0, "Up" )
        self.assertEqual( 4, score )
        self.assertEqual( 4, output[0][0] )
        self.assertEqual( 4, output[1][0] )

        input = [ [ 4, None ], [ 4, None ] ]
        output, score = practicum.handle_key_press( input, score, "Left" )
        self.assertEqual( 12, score )
        self.assertEqual( 8, output[0][0] )

        input = [ [ 8, None ], [ None, 2 ] ]
        output, score = practicum.handle_key_press( input, score, "Right" )
        self.assertEqual( 12, score )
        self.assertEqual( 8, output[1][0] )
        self.assertEqual( 2, output[1][1] )

        input = [ [ None, None ], [ 8, None ] ]
        output, score = practicum.handle_key_press( input, score, "Down" )
        self.assertEqual( 12, score )
        self.assertEqual( 8, output[1][1] )

    def test_handle_keypress_no_change(self):
        """
        This is one of the tests that could fail occasionally even if your code is completely correct.
        """
        input = [ [ 2, None ], [ None, None ] ]
        direction = [ "Up", "Left" ]
        for i in range( 0, 9999 ):
            output, score = practicum.handle_key_press( input, 0, direction[ i % 2 ] )
            self.assertEqual( input, input )
            self.assertEqual( 0, score )

    def test_handle_keypress_change(self):
        """
        This is one of the tests that could fail occasionally even if your code is completely correct.
        """
        input = [ [ 2, None ], [ None, None ] ]
        direction = [ "Right", "Left" ]
        found_insert = False
        for i in range( 0, 9999 ):
            output, score = practicum.handle_key_press( input, 0, direction[ i % 2 ] )
            self.assertNotEqual( input, output )
            if self._calculate_not_nones( output ) > 1:
                found_insert = True
                break
            else:
                input = output
        self.assertTrue( found_insert )

    def test_handle_keypress_score_and_match(self):
        input = [ [ 2, 2 ], [ 2, 2 ] ]
        output, score = practicum.handle_key_press( input, 0, "Up" )
        self.assertEqual( 8, score )

        input = [ [ 2, 4 ], [ 8, 8 ] ]
        output, score = practicum.handle_key_press( input, 1, "Down" )
        self.assertEqual( 17, score )

        input = [ [ None, 2, None, 2 ], [ None, None, 4, 2 ], [ None, None, 4, 2 ], [ None, 2, None, 2 ] ]
        output, score = practicum.handle_key_press( input, 0, "Left" )
        self.assertEqual( 20, score )
        self.assertEqual( [ 4, 8, 4 ], output[0][1:] )
        self.assertEqual( 4, output[1][3] )

    def _calculate_not_nones(self, matrix):
        sum = 0
        for row in matrix:
            for el in row:
                if el is not None:
                    sum += 1
        return sum

    def _extract_elements(self,matrix):
        result = set()
        for row in matrix:
            for el in row:
                if el is not None:
                    result.add( el )
        return result

    def assertNotEmpty(self, matrix):
        self.assertNotEqual( 0, self._calculate_not_nones( matrix ) )

if __name__ == "__main__":
    unittest.main()