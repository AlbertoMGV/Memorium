import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MainPage } from '../';

import { Juego6inPage } from '../juego6in/juego6in';

/**
 * Generated class for the Juego6Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-juego6',
  templateUrl: 'juego6.html',
})
export class Juego6Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Juego6Page');
  }

  goGame() {
  	this.navCtrl.push('Juego6inPage');
  }

}
