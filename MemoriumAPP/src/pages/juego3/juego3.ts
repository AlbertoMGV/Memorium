import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MainPage } from '../';

import { Juego3inPage } from '../juego3in/juego3in';
/**
 * Generated class for the Juego3Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-juego3',
  templateUrl: 'juego3.html',
})
export class Juego3Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Juego3Page');
  }
  goGame() {
  	this.navCtrl.push('Juego3inPage');
  }
}
