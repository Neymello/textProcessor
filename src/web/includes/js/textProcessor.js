function submitForm(){
	var g = new Graph();
	
	$.ajax({
		dataType: "json",
		url: "/cgi/processor.py",
		data: $("form").serialize(),
		success: function(data){
			
				drawCharacterChart(data.characters);
			
			
				$("#graph").html("");
			
				g = new Graph();
				
				for(n in data.nodes){
					g.addNode(n);
				}
				
				var count = 1;
				for(i in data.edges){
					from = data.edges[i].vFrom
					to = data.edges[i].vTo
					weight = data.edges[i].weight
					g.addEdge(from,to,{directed:true,label:"  "+weight,stroke:'red',"label-style":{"font-size": 14,"stroke":"blue","font-weight":"bold"}});
				}
				
				layouter = new Graph.Layout.Spring(g);
				layouter.layout();
				
				var renderer = new Graph.Renderer.Raphael('graph', g, 400, 400);
				renderer.draw();
		}
	});
	
	return false;
}

function drawCharacterChart(data){
	
	$("#drawCharacterChart").html("");
	
    $.jqplot.config.enablePlugins = true;
    
    var yAxisValues = [];
    var xAxisValues = [];
    
    for(w in data){
    	xAxisValues.push(w);
    	yAxisValues.push(data[w]);
    }
     
    plot1 = $.jqplot('drawCharacterChart', [yAxisValues], {
        title: "Characters Graph",
        animate: !$.jqplot.use_excanvas,
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            pointLabels: { show: true }
        },
        axes: {
            xaxis: {
                renderer: $.jqplot.CategoryAxisRenderer,
                ticks: xAxisValues
            },
            yaxis: {
            	tickOptions: {formatString: '%d'}
            }
        },
        highlighter: { show: false }
    });
}