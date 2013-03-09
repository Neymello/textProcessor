function submitForm(){
	var g = new Graph();
	
	$("#status span").css("text-decoration","blink");
	$("#status span").html("Processing...");
	
	$.ajax({
		dataType: "json",
		url: "/cgi/processor.py",
		data: $("form").serialize(),
		success: function(data){
			
				drawCharacterChart(data.characters);
				drawNGramChart(data.nGrams);
				drawWordChart(data.words);
				
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
				
				var renderer = new Graph.Renderer.Raphael('graph', g, 1024, 400);				
				$("#graphTitle").show();
				renderer.draw();
				
				$("#status span").css("text-decoration","none");
				$("#status span").html("Ready!");
				
				$('html,body').animate(
					{
						scrollTop: $("#results").offset().top
					}, 2000);
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

function drawNGramChart(data){
	var dataToDisplay = []
	
	for(n in data){
		dataToDisplay.push([n,data[n]]);
	}
	
	var plot3 = jQuery.jqplot ('drawNGramsChart', [dataToDisplay],
	    {
	    	title: "3 words sequence (3-grams) Graph",
	      seriesDefaults: {
	        renderer: jQuery.jqplot.PieRenderer,
	        rendererOptions: {
	          showDataLabels: true,
	          dataLabels: 'value'
	        }
	      },
	      legend: { show:true, location: 'e' }
	    }
	  );
}

function drawWordChart(data){
	
	$("#drawWordsChart").html("");
	
    $.jqplot.config.enablePlugins = true;
    
    var yAxisValues = [];
    var xAxisValues = [];
    
    for(w in data){
    	xAxisValues.push(w);
    	yAxisValues.push(data[w]);
    }
     
    plot2 = $.jqplot('drawWordsChart', [yAxisValues], {
        title: "Words Graph",
        animate: !$.jqplot.use_excanvas,
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            pointLabels: { show: true }
        },
        axesDefaults:{
        	tickRenderer: $.jqplot.CanvasAxisTickRenderer ,
            tickOptions: {
            	angle: -30,
          	}
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