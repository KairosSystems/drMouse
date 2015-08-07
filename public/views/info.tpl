	<div class="container" id="main-container">
		<h1>Acerca de enfermedades</h1>

		<div class="row">
			<div class="col-md-8">
				<p>{{enfermedad}}</p>	
				
				<div class="row">
					<div class="col-md-12 text-enfermedad">
						<p class="info">{{texto}}</p>
						<br />
						<h4>Sintomas</h4>
						<ul>
						%for sintoma in sintomas:
							<li>{{sintoma}}</li>
						%end
						</ul>
					</div>
				</div>
			</div>
			<div class="col-md-4" >
				<img src="/static/images/lungs.jpg" />
			</div>
		</div>
		<br />
		
	</div>
