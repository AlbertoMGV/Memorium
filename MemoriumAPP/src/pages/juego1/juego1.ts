import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MainPage } from '../';

import { Juego1inPage } from '../juego1in/juego1in';
/**
 * Generated class for the Juego1Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-juego1',
  templateUrl: 'juego1.html',
})
export class Juego1Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Juego1Page');
  }
  goGame() {
  	this.navCtrl.push('Juego1inPage');
    //this.navCtrl.setRoot('Juego1inPage');
  }

}
