	<div class="container" id="main-container">
		<h1>Enfermedades</h1>
		<ul>
			%for enf in enfermedades:
				<li>
					<a href="/enfs/{{enf}}">{{enf}}</a>
				</li>
			%end
		</ul>		
	</div>
