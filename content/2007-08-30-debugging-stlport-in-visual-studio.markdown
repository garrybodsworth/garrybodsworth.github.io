Title: Debugging STLPort in Visual Studio - autoexp.dat
Date: 2007-08-30T21:28:00+00:00
Slug: debugging-stlport-in-visual-studio
Category: 
Tags: 
Authors: Garry Bodsworth

We use <a href="http://stlport.sourceforge.net/">STLPort</a> for our C++ standard library as it is substantially faster than the one supplied with Visual Studio 2005.  I  have expended quite a lot of energy trying to get the Microsoft STL to speed up more, with custom allocators and the suchlike.  The reason I pursued it was to make debugging easier as there was no way (by default) to look inside the containers in a structured fashion.

Then I realised I was approaching the problem from the wrong angle.  Perhaps Visual Studio allows us to customise the debugging visualisations, and that means using STLPort with all the debugging benefits of the in-built system.  This was where I discovered the <a href="http://www.developer.com/net/cplus/article.php/3509761">autoexp.dat</a> which is more or less undocumented by Microsoft.  The system allows you to create custom visualisers for any datatype in the debugger.  Unfortunately it requires arcane rituals to make it work and I believe the format may have changed for VS2005.

Anyway on to the meat of this post!  I will post here the code you need to visualise map, vector, set, and list in Visual Studio 2005.  First go and open <span style="font-weight:bold;">C:\Program Files\Microsoft Visual Studio 8\Common7\Packages\Debugger\autoexp.dat</span> in a text editor.  Locate the line featuring the text <span style="font-weight:bold;">PROPVARIANT</span>.  Just above that line add the following:
<pre>
;------------------------------------------------------------------------------
;  STLPORT visualisers
;------------------------------------------------------------------------------

;------------------------------------------------------------------------------

;  stlp_std::vector
;------------------------------------------------------------------------------
stlp_std::vector<*>{
    children
    (
        #array
        (
            expr :    ($c._M_start)[$i], 

            size :    $c._M_finish-$c._M_start
        )
    )
   
    preview
    (
        #(
            "[",
            $e._M_finish - $e._M_start ,
            "](",

           
            #array
            (
                expr :     ($c._M_start)[$i], 
                size :     $c._M_finish-$c._M_start
            ),
            ")"
        )

    )
}

;------------------------------------------------------------------------------
;  stlp_std::list
;------------------------------------------------------------------------------
stlp_std::list<*,*>{

    children
    (
        #list
        (
         head : $c._M_node._M_data._M_next,
         skip : &($c._M_node._M_data),
         next : _M_next
        ) : #( *($T1 *)(sizeof(stlp_std::priv::_List_node_base)+((char*)&($e))) )

    )
   
    preview
    (
     #(
      "(",
      #list
      (
       head : $c._M_node._M_data._M_next,
       skip : &($c._M_node._M_data),
       next : _M_next
      ) : *($T1 *)(sizeof(stlp_std::priv::_List_node_base)+((char*)&($e))),

      ")"
     )
    )
}

;------------------------------------------------------------------------------
;  stlp_std::set
;------------------------------------------------------------------------------

stlp_std::set<*> {
 children
 (
  #tree
  (
   head : $c._M_t._M_header._M_data._M_parent,
   skip : $c._M_t._M_header._M_data,
   left : _M_left,
   right : _M_right,
   size : $c._M_t._M_node_count

  ) : ((_Node*)(&$e))->_M_value_field
 )
}

;------------------------------------------------------------------------------
;  stlp_std::map
;------------------------------------------------------------------------------

stlp_std::map<*,*,*,*> {
 children
 (
  #(
   [map]: [$c,!],

   #tree
   (
    head : $c._M_t._M_header._M_data._M_parent,
    left : _M_left,
    right : _M_right,
    skip : $c._M_t._M_header._M_data

   ) : *(stlp_std::pair<$T1,$T2>*)(((char*)(&((*((stlp_std::priv::_Rb_tree_node<$T1>*)(&$e)))._M_value_field))))
  )
 )
}
</pre>

I am pretty sure I need to do some more tweaking to get it working even better.  The map implementation is certainly the best part as it displays the list of items as pairs of (key, value) which is really useful.  Some of the code for this was pilfered from the comments of <a href="http://www.virtualdub.org/blog/pivot/entry.php?id=120">this article</a> - thanks to those people who blazed the initial trail.