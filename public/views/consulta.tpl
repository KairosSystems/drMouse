	<div class="container" id="main-container">
		<h1>Consulta</h1>
		<div class="row">
			<div class="col-md-8">
				<p>{{pregunta}}</p>	
				
				<div class="row">
					<div class="col-md-4 botones">
						<a href="/consulta/no" class="btn btn-default">No</a>
						<a href="/consulta/no" class="btn btn-default">Casí nada</a>
						<a href="/consulta/si" class="btn btn-default">Un poco</a>
						<a href="/consulta/si" class="btn btn-default">si</a>
					</div>
					<div class="col-md-8">
					</div>
				</div>
			</div>
			<div class="col-md-4 div-enfs" >
				<p>Posibles Enfermedades</p>
				<ul>
					%for enf in enfermedades:
						<li>{{enf}}</li>
					%end
				</ul>
			</div>
		</div>
	</div>
