import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MainPage } from '../';

import { Juego2inPage } from '../juego2in/juego2in';
/**
 * Generated class for the Juego2Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-juego2',
  templateUrl: 'juego2.html',
})
export class Juego2Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Juego2Page');
  }
  goGame() {
  	this.navCtrl.push('Juego2inPage');
  }

}
