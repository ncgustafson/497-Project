// 'js/mian.js'

var slidershoesl_img = document.querySelector('.slidershoesl-img');
var shoelimages = ['a_temp.jpg', 'b_temp.jpg', 'c_temp.jpg', 'd_temp.jpg', 'e_temp.jpg'];
let i = 0;
var slidershoesr_img = document.querySelector('.slidershoesr-img');
var shoerimages = ['a_temp_left.jpg', 'b_temp_left.jpg', 'c_temp_left.jpg', 'd_temp_left.jpg', 'e_temp_left.jpg'];
let h = 0;
var sliderpants_img = document.querySelector('.sliderpants-img');
var pantsimages = ['pants1.jpg', 'shorts1.jpg', 'shorts2.jpg', 'swim1.jpg'];
let j = 0;
var slidershirt_img = document.querySelector('.slidershirt-img');
var shirtimages = ['shirt1.jpg', 'shirt2.jpg', 'sweater3.jpg', 'sweater1.jpg', 'tshirt1.jpg', 'tshirt2.jpg'];
let k = 0;

//Current Outfit Selectors
var curr_leftShoe = document.querySelector('.left');
var curr_rightShoe = document.querySelector('.right');
var curr_pants = document.querySelector('.pants');
var curr_shirt = document.querySelector('.shirt');
var curr_outfit = ['', '', '', '']

function shoelPrev(){
	if(i <= 0) i = shoelimages.length;
	i--;
	return shoelSetImg();
}

function shoelNext(){
	if(i >= shoelimages.length-1) i = -1;
	i++;
	return shoelSetImg();
}

function shoelSetImg(){
	slidershoesl_img.setAttribute('src', "images/"+shoelimages[i]);
	return;

}

function shoerPrev(){
	if(h <= 0) h = shoerimages.length;
	h--;
	return shoerSetImg();
}

function shoerNext(){
	if(h >= shoerimages.length-1) h = -1;
	h++;
	return shoerSetImg();
}

function shoerSetImg(){
	slidershoesr_img.setAttribute('src', "images/"+shoerimages[h]);
	return;

}

function pantPrev(){
	if(j <= 0) j = pantsimages.length;
	j--;
	return pantSetImg();
}

function pantNext(){
	if(j >= pantsimages.length-1) j = -1;
	j++;
	return pantSetImg();
}

function pantSetImg(){
	return sliderpants_img.setAttribute('src', "images/"+pantsimages[j]);

}

function shirtPrev(){
	if(k <= 0) k = shirtimages.length;
	k--;
	return shirtSetImg();
}

function shirtNext(){
	if(k >= shirtimages.length-1) k = -1;
	k++;
	return shirtSetImg();
}

function shirtSetImg(){
	return slidershirt_img.setAttribute('src', "images/"+shirtimages[k]);
}

function apply(letter) {
	switch (letter) {
		case 'l':
			//Left Shoe
			console.log("LeftShoe: " + slidershoesl_img.getAttribute('src'));
			curr_outfit[0] = slidershoesl_img.getAttribute('src');
			return curr_leftShoe.setAttribute('src', slidershoesl_img.getAttribute('src'));
		case 'r':
			//Right Shoe
			console.log("RightShoe: " + slidershoesr_img.getAttribute('src'));
			curr_outfit[0] = slidershoesr_img.getAttribute('src');
			return curr_rightShoe.setAttribute('src', slidershoesr_img.getAttribute('src'));
			/*console.log("RightShoe: " + shoerimages[h], h);
			curr_outfit[1] = shoerimages[h];
			return curr_rightShoe.setAttribute('src', "images/"+shoerimages[h]);*/
		case 'p':
			//
			// curr_outfit[2] = shirtimages[k];
			curr_outfit[2] = sliderpants_img.getAttribute('src');
			return curr_pants.setAttribute('src', sliderpants_img.getAttribute('src'));
		default:
			//Shirt
			console.log("Shirt: " + slidershirt_img.getAttribute('src'));
			curr_outfit[3] = slidershirt_img.getAttribute('src');
			return curr_shirt.setAttribute('src', slidershirt_img.getAttribute('src'));
	}
}

// function changeCategory(letter) {
// 	switch(letter) {
// 		case 'l':
// 			//Left Shoe
// 			var x = document.getElementById('leftCat').value;
// 			switch (x) {
// 				case 'all':
// 					shoelimages = ['a_left.jpg', 'b.jpg', 'c_left.jpg', 'd.jpg', 'e_left.jpg'];
// 					return;
// 				case 'casual':
// 					shoelimages = ['d.jpg'];
// 					return;
// 				case 'formal':
// 					shoelimages = ['c_left.jpg'];
// 					return;
// 			}
// 		case 'r':
// 			//Right Shoe
// 			var x = document.getElementById('rightCat').value;
// 			switch (x) {
// 				case 'all':
// 					shoelimages = ['a_left.jpg', 'b.jpg', 'c_left.jpg', 'd.jpg', 'e_left.jpg'];
// 					return;
// 				case 'casual':
// 					shoelimages = ['d.jpg'];
// 					return;
// 				case 'formal':
// 					shoelimages = ['c_left.jpg'];
// 					return;
// 			}
// 		case 'p':
// 			//Pants
// 		default:
// 			//Shirt
// 	}
// }